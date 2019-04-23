import asyncio
import websockets
import json


async def test_success_registration():
    async with websockets.connect(
            'ws://localhost:8080') as websocket:

        correct_creds = {
                "Type": "registration",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Status": "success"}


async def test_success_login():
    async with websockets.connect(
            'ws://localhost:8080') as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Status": "success"}


async def test_failture_login():
    async with websockets.connect(
            'ws://localhost:8080') as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user123",
                "Password": "password123"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Status": "error"}


async def test_failture_password():
    async with websockets.connect(
            'ws://localhost:8080') as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password123"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Status": "error"}

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        test_success_login(),
        test_success_registration(),
        test_failture_login(),
        test_failture_password(),
    ))

# loop.run_until_complete(asyncio.gather(*[test_login() for _ in range(100)]))
