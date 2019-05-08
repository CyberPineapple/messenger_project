import logging as log
from peewee_async import Manager
from aioredis import create_pool
from aiohttp import web
from aiohttp_session import session_middleware, setup
from aiohttp_session.redis_storage import RedisStorage

from tools.models import database
from tools.json_validator import loads, is_json
from tools.sessions import request_user
from accounts.models import User
from accounts.views import Register, LogIn, LogOut
from chat.models import Chat, Message
from chat.views import ActionChat

# TODO: goto active_sockets -> dict()
# it's need for send messages to current chat


    # sessions maybe problem becouse middleware not work in websockets
    # once request and talk

    # request object contain:
        # app -- settings db and kv store
            # manager -- async db manager
        # session -- result method get_session()
        # username_session -- session.get("user")
        # user -- if username_session then object from db
        # chat -- current chat when "Command: Choise"
        # active_sockets -- store for websockets

async def websocket_handler(request):

    app = request.app
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    request.app.websocket = ws
    #app.active_sockets.append(ws)
    # user = request.session.get("user")
    # chat = request.session.get("chat")
    # if chat not in app.active_sockets.keys():
    #     app.active_sockets[chat] = {} # -> {"name_chat":{"user_id": ws}}

    # log.debug(request.session.get("user"))
    # log.debug(dir(app))
    # log.debug(f"request = {request}")
    # log.debug(f"app.redis = {app.redis_pool}")
    # log.debug(f"app.manager = {app.manager}")  # async db manager
    # contain websockets
    log.debug(f"app.active_sockets = {app.active_sockets}")

    # action with session
    # from aiohttp_session import get_session
    # session = await get_session(request)
    # log.debug(f"{session}")
    # session['counter'] = (session.get('counter') or 0) + 1
    # assert "counter" in session
    # log.debug(f"{session['counter']}")

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT and await is_json(msg.data):


            user = request.session.get("user")
            chat = request.session.get("chat")
            print(user, chat)

            log.debug(msg.data)
            jdata = loads(msg.data)

            if jdata["Type"] == "close":
                # TODO: test close field
                await ws.send_json({"Status": "close"})
                app.active_sockets[chat].pop(user)
                # app.active_sockets.remove(ws)
                log.debug(app.active_sockets)
                await ws.close()

            elif jdata["Type"] == "logout":
                data = await LogOut(request).logout()
                await ws.send_json(data)
                log.debug(app.active_sockets)
                #app.active_sockets.remove(ws)
                await ws.close()

            elif jdata["Type"] == "registration":
                # TODO: check setting session after reg
                data = await Register(request).create_user(**jdata)
                await ws.send_json(data)

            elif jdata["Type"] == "login":
                # TODO: check setting session after login
                # two send_json, compare in one json
                data = await LogIn(request).loginning(**jdata)
                await ws.send_json(data)
                data = await Chat.all_chats(request.app.manager)
                await ws.send_json(data)
                await ws.close()

            elif jdata["Type"] == "chat":
                data = {}
                # TODO: CRUD chat
                if "Command" in jdata.keys():
                    if jdata["Command"] == "message":
                        data = await ActionChat(request).send_message(**jdata)
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
                        pass

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
            RedisStorage(redis_pool)),
        request_user]
    app = web.Application(middlewares=middleware)
    setup(app, storage)
    app.add_routes([web.get("/", websocket_handler)])

    #app.active_sockets = []
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
