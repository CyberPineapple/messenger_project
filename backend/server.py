# Commnand to run the server
#  $ gunicorn -c settings.ini  server:main
#                       --worker-class aiohttp.worker.GunicornWebWorker
#

import logging as log

from accounts.models import User
from accounts.views import LogIn, LogOut, Register
from aiohttp import web
from aiohttp_session import session_middleware, setup
from aiohttp_session.redis_storage import RedisStorage
from aioredis import create_pool
from chat.models import Chat, Message
from chat.views import ActionChat
from peewee_async import Manager
from tools.json_validator import is_json, loads
from tools.models import database
from tools.sessions import request_user_middleware
from tools.store_users import StoreActiveChats

# TODO:
# check eof ws
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


class BaseClass:
    def __init__(self, command, ws, request):
        self._command = command
        self.ws = ws
        self.request = request

    async def commandy(self, **kwarg):
        try:
            func = getattr(self, self._command)
            return await func(**kwarg)
        except AttributeError as ae:
            print("AttributeError", ae)


class JSONAccount(BaseClass):
    async def login(self, **jdata):
        data = await LogIn(self.request).loginning(**jdata)
        await self.ws.send_json(data)

        if data["Status"] == "success":
            data = await Chat.all_chats(self.request.app.manager)
            return data

    async def logout(self, **jdata):
        # TODO: may be bug ws close before send data
        data = await LogOut(self.request).logout()
        if not self.ws.closed:
            await self.ws.close()
        return data

    async def registration(self, **jdata):
        return await Register(self.request).create_user(**jdata)


class JSONChat(BaseClass):
    async def message(self, **jdata):
        await ActionChat(self.request).send_message(**jdata)

    async def choice(self, **jdata):
        return await ActionChat(self.request).send_messages_from_chat(**jdata)

    async def create(self, **jdata):
        data = await ActionChat(self.request).create_chat(**jdata)
        await self.ws.send_json(data)
        return await self.list()

    async def list(self, **jdata):
        return await ActionChat(self.request).send_list_chats()

    async def delete(self, **jdata):
        return await ActionChat(self.request).delete_chat()

    async def earlier(self, **jdata):
        return await ActionChat(self.request).earlier_messages()

    async def connected(self, **jdata):
        return await ActionChat(self.request).send_list_online_users()

    async def purge(self, **jdata):
        return await ActionChat(self.request).purge_messages()


public_types = {"account": JSONAccount, "chat": JSONChat}


async def websocket_handler(request):

    # app = request.app
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT and await is_json(msg.data):

            request.app.websocket = ws
            # log.debug(msg.data)
            jdata = loads(msg.data)
            router = public_types.get(jdata["Type"])(jdata["Command"], ws,
                                                     request)
            responce = await router.commandy(**jdata)
            if responce is not None:
                await ws.send_json(responce)

            # log.debug(
            #     f"""app.active_sockets = {app.active_sockets.all_chats()}""")

            # else is comment becouse
            # else:
            #    await ws.send_json({"Status": "error in json file"})

        elif msg.type == web.WSMsgType.ERROR:
            print("Connection closed with exception %s" % ws.exception())

    return ws


async def init():
    redis = await create_pool("redis://localhost")
    storage = RedisStorage(redis)
    middleware = [
        session_middleware(RedisStorage(redis)), request_user_middleware
    ]
    app = web.Application(middlewares=middleware)
    setup(app, storage)
    app.add_routes([web.get("/", websocket_handler)])

    app.active_sockets = StoreActiveChats()
    DATABASE = {
        "database": "messenger",
        "password": "sl+@lM!93nd3_===",
        "user": "user",
        "host": "localhost",
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
        format="%(levelname)s %(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )

    return app


async def main():
    return await init()


if __name__ == "__main__":
    web.run_app(init())
