import asyncio
import websockets
import json

host = "ws://localhost:8080"
#host = "ws://host-94-103-84-32.hosted-by-vdsina.ru:8080"


async def success_register(websocket):

    correct_creds = {
            "Type": "registration",
            "Login": "user",
            "Password": "password"
    }

    await websocket.send(json.dumps(correct_creds))
    print(f"R: {correct_creds}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def success_signin(websocket):

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

    chat_list = await websocket.recv()
    print(f"2A: {chat_list}")
    print("2A: There no assert")


async def success_logout(websocket):

    logout_data = {
        "Type": "logout",
        "Login": "user"
    }

    await websocket.send(json.dumps(logout_data))
    print(f"R: {logout_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    assert json.loads(answer) == {"Type": "logout", "Status": "success"}


async def failture_login(websocket, uncorrect_creds=None):
    """
    By default user exist, but password is uncorrect.
    If need uncorrect user, use arg uncorrect_creds.
    Type(uncorrect_creds) -> dict
    """

    if uncorrect_creds is None:
        uncorrect_creds = {
                "Type": "login",
                "Login": "user",
                "Password": "password123"
        }

    await websocket.send(json.dumps(uncorrect_creds))
    print(f"R: {uncorrect_creds}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    assert json.loads(answer) == {"Type": "login", "Status": "error"}


async def success_create_chat(websocket, chat_data=None):
    if chat_data is None:

        chat_data = {
            "Type": "chat",
            "Command": "create",
            "Chat": "general",
        }

    await websocket.send(json.dumps(chat_data))
    print(f"R: {chat_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")

    chat_list = await websocket.recv()
    print(f"A: {chat_list}")
    print("There no assert")


async def success_create_close_chat(websocket, chat_data=None):
    if chat_data is None:

        chat_data = {
            "Type": "chat",
            "Command": "create",
            "Chat": "secret general",
            "Password": "secret"
        }

    await websocket.send(json.dumps(chat_data))
    print(f"R: {chat_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")
    chat_list = await websocket.recv()
    print(f"A: {chat_list}")
    print("There no assert")


async def send_chat_list(websocket, data=None):
    if data is None:
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


async def choice_chat(websocket, data=None):

    if data is None:

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "general"}

    await websocket.send(json.dumps(data))
    print(f"R: {data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def choice_close_chat(websocket, data=None):

    if data is None:

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "general",
                "Password": "secret"}

    await websocket.send(json.dumps(data))
    print(f"R: {data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def send_message(websocket, message_data):
    if message_data is None:

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


async def test_success_registration():
    async with websockets.connect(
            host) as websocket:
        await success_register(websocket)


async def test_exists_registration():
    """
    Not used success_register, becouse
    asserts.
    """
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
            "Status": "user exist"
        }


async def test_success_sign_in():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)


async def test_failture_sign_in_bad_password():
    async with websockets.connect(
            host) as websocket:

        await failture_login(websocket)


async def test_failture_sign_in_user_not_exist():
    async with websockets.connect(
            host) as websocket:

        uncorrect_creds = {
                "Type": "login",
                "Login": "user123",
                "Password": "password123"
        }

        await failture_login(websocket, uncorrect_creds)


async def test_succsses_logout():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)
        await success_logout(websocket)


async def test_failture_logout():
    """
    User not sign in
    """
    async with websockets.connect(
            host) as websocket:

        await success_logout(websocket)


async def test_succsses_create_chat():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)
        await success_create_chat(websocket)

async def test_failed_create_chat():
    """
    User not sign in
    """
    async with websockets.connect(
            host) as websocket:

        chat_data = {
            "Type": "chat",
            "Command": "create",
            "Chat": "boltaika",
        }

        await success_create_chat(websocket, chat_data)


async def test_success_create_close_chat():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)
        await success_create_close_chat(websocket)


async def test_success_send_chat_list():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)

        await send_chat_list(websocket)


async def test_nonauth_get_chat_list():
    async with websockets.connect(
            host) as websocket:

        await send_chat_list(websocket)


async def test_success_choise_chat():

    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)

        await choice_chat(websocket)


async def test_success_enter_in_closed_chat():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)

        await choice_chat(websocket)


async def test_failed_enter_in_closed_chat():
    """
    Field password not in json request
    """
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "secret general"
                }

        await choice_close_chat(websocket, data)


async def test_failed_enter_in_closed_chat_bad_pass():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)

        data = {"Type": "chat",
                "Command": "choice",
                "Chat": "secret general",
                "Password": "terces"
                }

        await choice_close_chat(websocket, data)


async def test_success_send_message():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)
        await choice_chat(websocket)
        await send_message(websocket)
        await success_logout(websocket)


async def test_success_send_message_to_closed_chat():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)
        await choice_close_chat(websocket)
        await send_message(websocket)


async def test_reconnect():
    async with websockets.connect(
            host) as websocket:

        await success_signin(websocket)

    async with websockets.connect(
            host) as websocket:

        await choice_chat(websocket)
        await send_message(websocket)


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
    #await test_success_registration()
    await test_succsses_create_chat()
    #await test_success_create_close_chat()


loop = asyncio.get_event_loop()
# run one, becouse next, check # exist user
loop.run_until_complete(create_base_for_test())

loop.run_until_complete(
    asyncio.gather(
        # test_exists_registration(),
        # test_success_sign_in(),
        # test_failture_sign_in_user_not_exist(),
        # test_failture_sign_in_bad_password(),
        # test_succsses_logout(),
        # test_failture_logout(),
        # test_failed_create_chat(),
        # test_success_choise_chat(),
        # test_success_send_chat_list(),
        # test_success_send_message(),
        # test_success_send_message_to_closed_chat(),
        # test_failed_enter_in_closed_chat(),
        # test_failed_enter_in_closed_chat_bad_pass(),
        # test_success_enter_in_closed_chat(),
        # test_nonauth_get_chat_list(),
        # test_reconnect(),
        # test_failed_create_chat()#, test after realise redirect for non auth
        # test_fault_logout(),# not need becouse, if logout, then logout
        # test_multupule_connection(),
        ))
