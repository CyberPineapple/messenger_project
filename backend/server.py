from database import insert_db_user, extract_db_user, loop
from aiohttp import web
import asyncio

import json

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
        if msg.type == web.WSMsgType.TEXT and await is_json(msg.data):
            print(msg.data)
            jdata = json.loads(msg.data)
            if jdata["Type"] == "close":
                await ws.send_json({"Status": "close"})
                await ws.close()
            elif jdata["Type"] == "registration":
                await insert_db_user(**jdata)
                # send cookie
                await ws.send_json({"Type": "registration", "Status": "success"})
            elif jdata["Type"] == "login":
                credentials = await extract_db_user(**jdata)
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


app = web.Application()
app.add_routes(routes)

loop = asyncio.new_event_loop()
loop.create_task(web.run_app(app))

loop.run_forever()

