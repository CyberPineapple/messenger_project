from aiohttp import web
import aiosqlite
import sqlite3
from os import path


class Database:

    def __init__(self, dbname, tablename):
        self.dbname = dbname
        self.tablename = tablename
        if not path.isfile(dbname):
            self.create_table()

    def create_table(self):
        with sqlite3.connect(self.dbname) as db:
            db.execute("CREATE TABLE {table} \
                      (login text, password text)".format(
                      table=self.tablename))

    async def insert_db(self, login, password):
        '''
        Note: Duplicate!!
        '''
        async with aiosqlite.connect(self.dbname) as db:
            await db.execute(
                "INSERT INTO {table} VALUES('{login}', '{password}')".format(
                    login=login, password=password, table=self.tablename))
            await db.commit()

    async def extract_db_by_login(self, login):
        async with aiosqlite.connect(self.dbname) as db:
            async with db.execute("SELECT login, password FROM {table} \
                                   WHERE login='{login}' ".format(
                                       login=login, \
                                       table=self.tablename)) as cur:
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
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == web.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws

@routes.post('/login')
async def do_login(request):
    data = await request.post()
    login = data['login']
    password = data['password']
    await database.insert_db(login, password)
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
