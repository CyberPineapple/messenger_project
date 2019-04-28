import asyncio
import websockets
import json

host = "ws://localhost:8080"
# host = "ws://host-94-103-84-32.hosted-by-vdsina.ru:8080"


async def test_success_registration():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "registration",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        #assert json.loads(answer) == {
        #     "Type": "registration",
        #    "Status": "success"}


async def test_exists_registration():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "registration",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {
             "Type": "registration",
            "Status": "user exist"}


async def test_success_sign_in():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}


async def test_failture_sign_in():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user123",
                "Password": "password123"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "error"}


async def test_failture_password():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password123"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "error"}


async def test_succsses_logoout():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}


        logout_data = {
            "Type": "logout",
            "Login": "user"
        }

        await websocket.send(json.dumps(logout_data))
        print(f"> {logout_data}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "logout", "Status": "success"}


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
       test_success_registration(),
       test_exists_registration(),
       test_success_sign_in(),
       test_failture_sign_in(),
       test_failture_password(),
       test_succsses_logoout(),
    ))

# loop.run_until_complete(asyncio.gather(*[test_login() for _ in range(100)]))
