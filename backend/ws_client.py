import asyncio
import websockets
import json


async def hello():
    async with websockets.connect(
            'ws://localhost:8080') as websocket:

        data = {
                "Type": "reg",
                "Login": "login",
                "Password": "password"
        }

        await websocket.send(json.dumps(data))
        print(f"> {data}")

        answer = await websocket.recv()
        print(f"< {answer}")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*[hello() for _ in range(100)]))
