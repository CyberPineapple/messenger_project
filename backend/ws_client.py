import asyncio
import websockets
import json

host = "ws://localhost:8080"
# host = "ws://host-94-103-84-32.hosted-by-vdsina.ru:8080"


async def test_multupule_connection():
    async with websockets.connect(host) as ws:
        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await ws.send(json.dumps(correct_creds))
        print(f"> {correct_creds}")
        answer = await ws.recv()
        print(f"< {answer}")

        message_data = {
            "Type": "message",
            "User": "user",
            "Chat": "general1",
            "Text": "user: Hey, there is somebody?"
        }

        await ws.send(json.dumps(message_data))
        print(f"> {message_data}")
        await asyncio.sleep(3)
        answer = await ws.recv()
        print(f"< {answer}")

    async with websockets.connect(host) as ws_1:

        register_creds = {
            "Type": "login",
            "Login": "admin",
            "Password": "admin"
        }

        await ws_1.send(json.dumps(register_creds))
        print(f"> {register_creds}")
        answer = await ws_1.recv()
        print(f"< {answer}")

        message_data = {
            "Type": "message",
            "User": "admin",
            "Chat": "general1",
            "Text": "admin: Yes, only me."
        }
        await ws_1.send(json.dumps(message_data))
        print(f"> {message_data}")
        await asyncio.sleep(2)
        answer = await ws_1.recv()
        print(f"< {answer}")

    # async with websockets.connect(host) as ws_2:
    #     message_data = {
    #         "Type": "message",
    #         "User": "user",
    #         "Chat": "general",
    #         "Text": "Hey, there is somebody?"
    #     }

    #     await ws_2.send(json.dumps(message_data))
    #     print(f"> {message_data}")

    #     message_data = {"Type": "close"}

    #     await ws_2.send(json.dumps(message_data))
    #     print(f"> {message_data}")

    #     answer = await ws_2.recv()
    #     print(f"< {answer}")
    #     message_data = {
    #         "Type": "message",
    #         "User": "user",
    #         "Chat": "general",
    #         "Text": "Hey, there is somebody?"
    #     }

    #     await ws_2.send(json.dumps(message_data))
    #     print(f"> {message_data}")

    #     message_data = {"Type": "close"}

    #     await ws_2.send(json.dumps(message_data))
    #     print(f"> {message_data}")
    #     answer = await ws_2.recv()
    #     print(f"< {answer}")


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
        assert json.loads(answer) == {
             "Type": "registration",
            "Status": "success"}


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


async def test_succsses_logout():
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


async def test_fault_logout():
    async with websockets.connect(
            host) as websocket:

        logout_data = {
            "Type": "logout",
            "Login": "user"
        }

        await websocket.send(json.dumps(logout_data))
        print(f"> {logout_data}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "logout", "Status": "error"}


async def test_succsses_send_message():
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

        message_data = {
            "Type": "message",
            "User": "user",
            "Chat": "general",
            "Text": "Hey, there is somebody?"
        }

        await websocket.send(json.dumps(message_data))
        print(f"> {message_data}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == message_data


async def test_failed_send_message():
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

        message_data = {
            "Type": "message",
            "User": "user",
            "Chat": "POCHANY",
            "Text": "Hey, there is somebody?"
        }

        await websocket.send(json.dumps(message_data))
        print(f"> {message_data}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {
            "Type": "chat", "Status": "chat not exist"}


async def test_succsses_create_chat():
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

        chat_data = {
            "Type": "chat",
            "User": "user",
            "Chat": "general1",
        }

        await websocket.send(json.dumps(chat_data))
        print(f"> {chat_data}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "chat", "Status": "success"}


async def test_failed_create_chat():
    async with websockets.connect(
            host) as websocket:

        chat_data = {
            "Type": "chat",
            "User": "user",
            "Chat": "boltaika",
        }

        await websocket.send(json.dumps(chat_data))
        print(f"> {chat_data}")

        answer = await websocket.recv()
        print(f"< {answer}")
        assert json.loads(answer) == {"Type": "chat", "Status": "chat exist"}
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        # run one, becouse next, check exist user
        # test_success_registration(),
        # test_exists_registration(),
        # test_success_sign_in(),
        # test_failture_sign_in(),
        # test_failture_password(),
        # test_succsses_logout(),
        # test_fault_logout(),# not need becouse, if logout, then logout
        # test_succsses_send_message(),
        # test_failed_send_message(),

        #  test_succsses_create_chat(),
        # test_failed_create_chat(), test after realise redirect for non auth
        # user
        test_multupule_connection(),
        test_multupule_connection(),
        ))

# loop.runi_until_complete(asyncio.gather(*[test_login() for _ in range(100)]))
