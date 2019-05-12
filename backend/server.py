import logging as log
from peewee_async import Manager
from aioredis import create_pool
from aiohttp import web
from aiohttp_session import session_middleware, setup
from aiohttp_session.redis_storage import RedisStorage

from tools.models import database
from tools.json_validator import loads, is_json
from tools.sessions import request_user_middleware
from accounts.models import User
from accounts.views import Register, LogIn, LogOut
from chat.models import Chat, Message
from chat.views import ActionChat

# TODO:
# hash for chats password
# check eof ws
# Before delete chat kick users from chat
# update after login/logout online users
# update after login data_last_online
# check one user by one login
# How users know about new created chat?

# request -- object contain:
# # app -- settings db and kv store
# # # manager -- async db manager
# # session -- result method get_session()
# # username_session -- session.get("user")
# # user -- object from db
# # chat -- current chat when "Command: Choise"
# # active_sockets -- store for websockets


async def websocket_handler(request):

    app = request.app
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    log.debug(f"app.active_sockets = {app.active_sockets}")

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT and await is_json(msg.data):

            request.app.websocket = ws
            log.debug(msg.data)
            jdata = loads(msg.data)

            if jdata["Type"] == "close":
                await ws.send_json({"Status": "close"})
                await ws.close()
                log.debug(app.active_sockets)

            elif jdata["Type"] == "logout":
                data = await LogOut(request).logout()
                await ws.send_json(data)
                await ws.close()
                log.debug(app.active_sockets)

            elif jdata["Type"] == "registration":
                data = await Register(request).create_user(**jdata)
                await ws.send_json(data)

            elif jdata["Type"] == "login":
                # two send_json, compare in one json
                data = await LogIn(request).loginning(**jdata)
                await ws.send_json(data)
                if data["Status"] == "success":
                    data = await Chat.all_chats(request.app.manager)
                    await ws.send_json(data)

            elif jdata["Type"] == "chat":
                # TODO: CRUD chat
                if "Command" in jdata.keys():
                    if jdata["Command"] == "message":
                        data = await ActionChat(request).send_message(**jdata)
                        log.debug(f"app.active_sockets = {app.active_sockets}")
                    elif jdata["Command"] == "choice":
                        data = await ActionChat(
                            request).send_messages_from_chat(**jdata)
                    elif jdata["Command"] == "create":
                        data = await ActionChat(request).create_chat(**jdata)
                        await ws.send_json(data)
                        data = await ActionChat(request).send_list_chats()
                    elif jdata["Command"] == "list":
                        # TODO: Non auth user can get all chats
                        # data = await ActionChat(request).send_chats_users()
                        data = await ActionChat(request).send_list_chats()
                    elif jdata["Command"] == "delete":
                        data = await ActionChat(request).delete_chat()
                # crutch
                if data is not None:
                    await ws.send_json(data)
            else:
                await ws.send_json({"Status": "error in json file"})

        elif msg.type == web.WSMsgType.ERROR:
            print("Connection closed with exception %s" %
                  ws.exception())

    return ws


async def init():
    redis = await create_pool("redis://localhost")
    storage = RedisStorage(redis)
    middleware = [
        session_middleware(
            RedisStorage(redis)),
        request_user_middleware]
    app = web.Application(middlewares=middleware)
    setup(app, storage)
    app.add_routes([web.get("/", websocket_handler)])

    app.active_sockets = {}
    DATABASE = {
        "database": "Messenger",
        "password": "sl+@lM!93nd3_===",
        "user": "user",
        "host": "localhost"
    }

    database.init(**DATABASE)
    app.database = database
    app.database.set_allow_sync(False)
    app.manager = Manager(app.database)

    with app.manager.allow_sync():
        User.create_table(True)
        Chat.create_table(True)
        Message.create_table(True)

    log.basicConfig(
        level=log.DEBUG,
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

    return app

if __name__ == "__main__":
    web.run_app(init())
