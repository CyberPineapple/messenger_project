from os import path

from aiohttp import web

import aiosqlite
import json


class Database:

    def __init__(self, dbname, tablename):
        self.dbname = dbname
        self.tablename = tablename
        if not path.isfile(self.dbname):
            self._create_table()

    def _create_table(self):
        import sqlite3
        with sqlite3.connect(self.dbname) as db:
            db.execute(f"CREATE TABLE {self.tablename} \
                      (Login text, Password text)")

    async def _exists(self, Login):
        async with aiosqlite.connect(self.dbname) as db:
            async with db.execute(
                f"SELECT Login FROM {self.tablename} \
                  WHERE  Login='{Login}'") as cur:
                if await cur.fetchone():
                    return True
                return False

    async def insert_db(self, **kwarg):
        Login = kwarg['Login']
        Password = kwarg['Password']
        # Type = kwarg['Type'] for update password
        async with aiosqlite.connect(self.dbname) as db:
            if not await self._exists(Login):
                await db.execute(
                    f"INSERT INTO {self.tablename} \
                      VALUES('{Login}', '{Password}')")
                await db.commit()

    async def extract_db_by_login(self, Login):
        async with aiosqlite.connect(self.dbname) as db:
            async with db.execute(f"SELECT Login, Password \
                                    FROM {self.tablename} \
                                    WHERE Login='{Login}' ") as cur:
                async for row in cur:
                    return row


routes = web.RouteTableDef()


async def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


@routes.get("/")
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            if await is_json(msg.data):
                jdata = json.loads(msg.data)
                if jdata["Type"] == "close":
                    await ws.send_json({"Status": "close"})
                    await ws.close()
                elif jdata["Type"] == "reg":
                    await database.insert_db(**jdata)
                    await ws.send_json({"Status": "success"})
                else:
                    await ws.send_json({"Status": "error in json file"})

        elif msg.type == web.WSMsgType.ERROR:
            print("Connection closed with exception %s" %
                  ws.exception())

    return ws


# @routes.post("/login")
# async def do_Login(request):
#     data = await request.post()
#     Login = data["Login"]
#     Password = data["Password"]
#     await database.insert_db(Login, Password)  # if login exist not warnings
#     data = await database.extract_db_by_login(Login)
    # return web.Response(
    #    text="Hello world, {}, you Password is {}".format(*data))

database = Database("mydatabase.db", "credentials")
app = web.Application()
app.add_routes(routes)

web.run_app(app)
