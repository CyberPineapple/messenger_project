from aiohttp import web
import aiosqlite
import sqlite3
from os import path


class Database:

    def __init__(self, dbname, tablename):
        self.dbname = dbname
        self.tablename = tablename
        if not path.isfile(self.dbname):
            self.create_table()

    def create_table(self):
        with sqlite3.connect(self.dbname) as db:
            db.execute(f"CREATE TABLE {self.tablename} \
                      (login text, password text)")

    async def exists(self, login):
        async with aiosqlite.connect(self.dbname) as db:
            async with db.execute(
                f"SELECT login FROM {self.tablename} \
                 WHERE login='{login}'") as cur:
                if await cur.fetchone():
                    return True
                return False

    async def insert_db(self, login, password):
        async with aiosqlite.connect(self.dbname) as db:
            if not await self.exists(login):
                await db.execute(
                    f"INSERT INTO {self.tablename} \
                      VALUES('{login}', '{password}')")
                await db.commit()

    async def extract_db_by_login(self, login):
        async with aiosqlite.connect(self.dbname) as db:
            async with db.execute(f"SELECT login, password FROM {self.tablename} \
                                   WHERE login='{login}' ") as cur:
                async for row in cur:
                    return row


routes = web.RouteTableDef()


@routes.get("/ws")
async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
                print('websocket connection closed')
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == web.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())
    return ws


@routes.post('/login')
async def do_login(request):
    data = await request.post()
    login = data['login']
    password = data['password']
    await database.insert_db(login, password)  # if exists not warnings
    data = await database.extract_db_by_login(login)
    return web.Response(
        text="Hello world, {}, you password is {}".format(*data))


@routes.get('/')
async def root_page(request):
    return web.Response(text="You on root page")

database = Database('mydatabase.db', 'credentials')
app = web.Application()
app.add_routes(routes)

web.run_app(app)
