from peewee_async import Manager
from json import loads
from aioredis import create_pool
from asyncio import get_event_loop
from aiohttp import web
from aiohttp_session import session_middleware
from aiohttp_session.redis_storage import RedisStorage

from database import database, insert_db_user, extract_db_user
from database import User, Message

async def is_json(myjson):
    try:
        loads(myjson)
    except ValueError:
        return False
    return True


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT and await is_json(msg.data):
            print(msg.data)
            jdata = loads(msg.data)
            if jdata["Type"] == "close":
                await ws.send_json({"Status": "close"})
                await ws.close()
            elif jdata["Type"] == "registration":
                await insert_db_user(app.objects,**jdata)
                # send cookie
                await ws.send_json({"Type": "registration", "Status": "success"})
            elif jdata["Type"] == "login":
                credentials = await extract_db_user(app.objects,**jdata)
                if credentials and jdata["Password"] == credentials[1]:
                    # send cookie
                    await ws.send_json({"Type": "login", "Status": "success"})
                else:
                    await ws.send_json({"Type": "login", "Status": "error"})
            else:
                await ws.send_json({"Status": "error in json file"})

        elif msg.type == web.WSMsgType.ERROR:
            print("Connection closed with exception %s" %
                  ws.exception())

    return ws


async def request_user_middleware(app,handler):
    pass


async def create_app(loop):
    redis_pool = await create_pool(("localhost", 6379), loop=loop)
    # middleware = [session_middleware(RedisStorage(redis_pool)),request_user_middleware] # add check user
    app = web.Application()#middlewares=middleware)
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

    with app.objects.allow_sync():
        User.create_table(True)
        Message.create_table(True)

    return app

if __name__ == "__main__":
    loop = get_event_loop()
    app = loop.run_until_complete(create_app(loop))

    loop.create_task(web.run_app(app))
    loop.run_forever()
