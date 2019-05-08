import asyncio
import websockets
import json

host = "ws://localhost:8080"
#host = "ws://host-94-103-84-32.hosted-by-vdsina.ru:8080"


async def test_success_registration():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "registration",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {
             "Type": "registration",
            "Status": "success"
        }


async def test_exists_registration():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "registration",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
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
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}


async def test_failture_password():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password123"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "error"}


async def test_failture_sign_in():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user123",
                "Password": "password123"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
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
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        logout_data = {
            "Type": "logout",
            "Login": "user"
        }

        await websocket.send(json.dumps(logout_data))
        print(f"R: {logout_data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "logout", "Status": "success"}


async def test_fault_logout():
    async with websockets.connect(
            host) as websocket:

        logout_data = {
            "Type": "logout",
            "Login": "user"
        }

        await websocket.send(json.dumps(logout_data))
        print(f"R: {logout_data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "logout", "Status": "error"}


async def test_succsses_create_chat():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        chat_data = {
            "Type": "chat",
            "User": "user",
            "Command": "create",
            "Chat": "general",
        }

        await websocket.send(json.dumps(chat_data))
        print(f"R: {chat_data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "chat", "Status": "success"}


async def test_failed_create_chat():
    async with websockets.connect(
            host) as websocket:

        chat_data = {
            "Type": "chat",
            "User": "user123",
            "Chat": "boltaika",
        }

        await websocket.send(json.dumps(chat_data))
        print(f"R: {chat_data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {}


async def test_success_create_close_chat():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {"Type": "chat",
                "Command": "create",
                "Chat": "secret general",
                "Password": "secret"}

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")


async def test_success_send_chat_list():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {
            "Type": "chat",
            "Chat": "general",
            "Command": "list"
        }

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")
        #assert json.loads(answer) == {"Type": "login", "Status": "success"}


async def test_nonauth_get_chat_list():
    async with websockets.connect(
            host) as websocket:
        data = {
            "Type": "chat",
            "Chat": "general",
            "Command": "list"
        }

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")
        #assert json.loads(answer) == {"Type": "login", "Status": "success"}


async def test_success_choise_chat():

    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}
        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "general"}

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")


async def test_success_enter_in_closed_chat():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "secret general",
                "Password": "secret"
                }

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")


async def test_failed_enter_in_closed_chat():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "secret general"
                }

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")


async def test_failed_enter_in_closed_chat_bad_pass():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "secret general",
                "Password": "terces"
                }

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")


async def test_success_send_message():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "general"}

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")

        message_data = {
            "Type": "chat",
            "Command": "message",
            "Text": "Hey, there is somebody?"
        }

        await websocket.send(json.dumps(message_data))
        print(f"R: {message_data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        message_data["Status"] = "success"
        assert json.loads(answer) == message_data


async def test_success_send_message_to_closed_chat():
    async with websockets.connect(
            host) as websocket:

        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {"Type": "login", "Status": "success"}

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "secret general",
                "Password": "secret"}

        await websocket.send(json.dumps(data))
        print(f"R: {data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        print("There no assert")

        message_data = {
            "Type": "chat",
            "Command": "message",
            "Text": "Hey, there is somebody?"
        }

        await websocket.send(json.dumps(message_data))
        print(f"R: {message_data}")

        answer = await websocket.recv()
        print(f"A: {answer}")
        message_data["Status"] = "success"
        assert json.loads(answer) == message_data


async def test_multupule_connection():
    async with websockets.connect(host) as ws:
        correct_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password"
        }

        await ws.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")
        answer = await ws.recv()
        print(f"A: {answer}")

        message_data = {
            "Type": "message",
            "User": "user",
            "Chat": "general1",
            "Text": "user: Hey, there is somebody?"
        }

        await ws.send(json.dumps(message_data))
        print(f"R: {message_data}")
        await asyncio.sleep(3)
        answer = await ws.recv()
        print(f"A: {answer}")

    async with websockets.connect(host) as ws_1:

        register_creds = {
            "Type": "login",
            "Login": "admin",
            "Password": "admin"
        }

        await ws_1.send(json.dumps(register_creds))
        print(f"R: {register_creds}")
        answer = await ws_1.recv()
        print(f"A: {answer}")

        message_data = {
            "Type": "message",
            "User": "admin",
            "Chat": "general1",
            "Text": "admin: Yes, only me."
        }
        await ws_1.send(json.dumps(message_data))
        print(f"R: {message_data}")
        await asyncio.sleep(2)
        answer = await ws_1.recv()
        print(f"A: {answer}")


async def create_base_for_test():
    await test_success_registration()
    await test_succsses_create_chat()
    await test_success_create_close_chat()


loop = asyncio.get_event_loop()
# run one, becouse next, check # exist user
# loop.run_until_complete(create_base_for_test())

loop.run_until_complete(
    asyncio.gather(
        # test_exists_registration(),
        test_success_sign_in(),
        # test_failture_sign_in(),
        # test_failture_password(),
        # test_succsses_logout(),
        # test_success_choise_chat(),
        # test_success_send_chat_list(),
        # test_success_send_message(),
        # test_success_send_message_to_closed_chat(),
        # test_failed_send_message(),
        # test_success_send_message_in_closed_chat(),
        # test_failed_enter_in_closed_chat(),
        # test_failed_enter_in_closed_chat_bad_pass(),
        # test_success_enter_in_closed_chat(),
        # test_nonauth_get_chat_list()
        # test_failed_create_chat()#, test after realise redirect for non auth
        # test_fault_logout(),# not need becouse, if logout, then logout
        # test_multupule_connection(),
        ))
