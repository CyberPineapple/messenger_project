from peewee_async import Manager
from aioredis import create_pool
from asyncio import get_event_loop
from aiohttp import web
from aiohttp_session import session_middleware
from aiohttp_session.redis_storage import RedisStorage
import logging

from tools.models import database
from tools.json_validator import loads, is_json
from tools.actions_db import insert_db_user, extract_db_user
from tools.sessions import request_user_middleware
from accounts.models import User
from accounts.views import Register, LogIn
from chat.models import Chat, Message

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT and await is_json(msg.data):
            logging.debug(msg.data)
            jdata = loads(msg.data)

            if jdata["Type"] == "close":
                await ws.send_json({"Status": "close"})
                await ws.close()

            elif jdata["Type"] == "registration":
                if await Register(request).create_user(**jdata):
                    await ws.send_json({"Type": "registration", "Status": "success"})
                else:
                    await ws.send_json({"Type": "registration", "Status": "user exist"})

            elif jdata["Type"] == "login":
                if await LogIn(request).loginning(**jdata):
                    await ws.send_json({"Type": "login", "Status": "success"})
                else:
                    await ws.send_json({"Type": "login", "Status": "error"})
            else:
                await ws.send_json({"Status": "error in json file"})

        elif msg.type == web.WSMsgType.ERROR:
            print("Connection closed with exception %s" %
                  ws.exception())

    return ws



async def create_app(loop):
    redis_pool = await create_pool(("localhost", 6379), loop=loop)
    middleware = [session_middleware(RedisStorage(redis_pool)),request_user_middleware] # add check user
    app = web.Application(middlewares=middleware)
    app.redis_pool = redis_pool
    app.add_routes([web.get("/", websocket_handler)])


    DATABASE = {
        "database": "Messenger",
        "password": "sl+@lM!93nd3_===",
        "user": "user",
        "host": "localhost"
    }

    database.init(**DATABASE)
    app.database = database
    app.database.set_allow_sync(False)
    app.objects = Manager(app.database)



    return app

if __name__ == "__main__":
    loop = get_event_loop()
    app = loop.run_until_complete(create_app(loop))

    with app.objects.allow_sync():
        User.create_table(True)
        Chat.create_table(True)
        Message.create_table(True)

    logging.basicConfig(level=logging.DEBUG)
    loop.create_task(web.run_app(app))
    loop.run_forever()
