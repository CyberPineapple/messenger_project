import asyncio
from random import choice, randint
from string import ascii_letters

import websockets
from ws_client import (choice_chat, host, send_message,
                       success_signin)


async def genBoolShit():

    n = randint(4, 10)
    s = "".join(choice(ascii_letters) for x in range(randint(n - 1, n)))

    return s


async def bench_send_message(N):
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)
        await choice_chat(websocket)

        for i in range(N):
            text = await genBoolShit()
            message_data = {"Type": "chat", "Command": "message", "Text": text}

            await send_message(websocket, message_data)


loop = asyncio.get_event_loop()

loop.run_until_complete(bench_send_message(1000))
# After refractor conditional
# localhost:
#   max 75mes/1sec
#   avg 65mes/1sec
#   22-25sec/2000mes
#
# remote:
#   max 77 mes/1sec
#   avg 67mes/1sec
#   30sec/2000mes
