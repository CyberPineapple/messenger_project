import asyncio
import json

import websockets

host = "ws://localhost:8000"


host = "ws://messenger.servehttp.com:80/"
async def success_register(websocket, register_creds=None):

    if register_creds is None:

        register_creds = {
            "Type": "account",
            "Command": "registration",
            "Login": "user",
            "Password": "password",
        }

    await websocket.send(json.dumps(register_creds))
    print(f"R: {register_creds}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def success_signin(websocket, signin_creds=None):

    if signin_creds is None:

        signin_creds = {
            "Type": "account",
            "Command": "login",
            "Login": "user",
            "Password": "password"
        }

    await websocket.send(json.dumps(signin_creds))
    print(f"R: {signin_creds}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    assert json.loads(answer) == {
        "Type": "account",
        "Command": "login",
        "Status": "success"
    }

    chat_list = await websocket.recv()
    print(f"2A: {chat_list}")
    print("2A: There no assert")


async def success_logout(websocket, failture=False):

    logout_data = {"Type": "account", "Command": "logout"}

    await websocket.send(json.dumps(logout_data))
    print(f"R: {logout_data}")

    if failture:
        answer = await websocket.recv()
        print(f"A: {answer}")

        assert json.loads(answer) == {
            "Type": "account",
            "Command": "logout",
            "Status": "error"
        }
    else:
        answer = await websocket.recv()
        print(f"A: {answer}")
        assert json.loads(answer) == {
            "Type": "account",
            "Command": "logout",
            "Status": "success"
        }


async def failture_login(websocket, uncorrect_creds=None):
    """
    By default user exist, but password is uncorrect.
    If need uncorrect user, use arg uncorrect_creds.
    Type(uncorrect_creds) -> dict
    """

    if uncorrect_creds is None:
        uncorrect_creds = {
            "Type": "account",
            "Command": "login",
            "Login": "user",
            "Password": "password123"
        }

    await websocket.send(json.dumps(uncorrect_creds))
    print(f"R: {uncorrect_creds}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    assert json.loads(answer) == {
        "Type": "account",
        "Command": "login",
        "Status": "error"
    }


async def success_create_chat(websocket, chat_data=None, reson=True):
    """
    Arg reson need for evasion crush test, when non auth user
    try create chat, server send one json with Status: error
    """

    if chat_data is None:

        chat_data = {"Type": "chat", "Command": "create", "Chat": "general"}

    await websocket.send(json.dumps(chat_data))
    print(f"R: {chat_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")

    if reson:
        chat_list = await websocket.recv()
        print(f"A: {chat_list}")
        print("There no assert")


async def success_create_close_chat(websocket, chat_data=None):

    if chat_data is None:

        chat_data = {
            "Type": "chat",
            "Command": "create",
            "Chat": "secret general",
            "Password": "secret",
        }

    await websocket.send(json.dumps(chat_data))
    print(f"R: {chat_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")
    chat_list = await websocket.recv()
    print(f"A: {chat_list}")
    print("There no assert")


async def delete_chat(websocket):
    chat_data = {"Type": "chat", "Command": "delete"}

    await websocket.send(json.dumps(chat_data))
    print(f"R: {chat_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def send_chat_list(websocket, data=None):
    if data is None:
        data = {"Type": "chat", "Chat": "general", "Command": "list"}

    await websocket.send(json.dumps(data))
    print(f"R: {data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def choice_chat(websocket, data=None):

    if data is None:

        data = {"Type": "chat", "Command": "choice", "Chat": "general"}

    await websocket.send(json.dumps(data))
    print(f"R: {data}")

    messages = await websocket.recv()
    print(f"A: {messages}")
    print("There no assert")


async def choice_close_chat(websocket, data=None):

    if data is None:

        data = {
            "Type": "chat",
            "Command": "choice",
            "Chat": "secret general",
            "Password": "secret",
        }

    await websocket.send(json.dumps(data))
    print(f"R: {data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    print("There no assert")


async def send_message(websocket, message_data=None):
    if message_data is None:

        message_data = {
            "Type": "chat",
            "Command": "message",
            "Text": "Hey, there is somebody?",
        }

    await websocket.send(json.dumps(message_data))
    print(f"R: {message_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    # json_answer = json.loads(answer)
    # assert json_answer == message_data
    print("There no assert")


async def send_message_next_page(websocket):

    message_data = {"Type": "chat", "Command": "earlier"}

    await websocket.send(json.dumps(message_data))
    print(f"R: {message_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")
    # json_answer = json.loads(answer)
    # assert json_answer == message_data
    print("There no assert")


async def send_image(websocket, message_data=None):
    with open('static/pica.png', 'rb') as image:
        import base64
        image = base64.encodebytes(image.read()).decode()
        image = "data:image/png;base64," + image

    if message_data is None:
        message_data = {
            "Type": "chat",
            "Command": "message",
        }

        message_data["Image"] = image
    await send_message(websocket, message_data)


async def get_requests(websocket):

    answer = await websocket.recv()
    print(f"A: {answer}")


async def send_custom_json(websocket, json_data):
    await websocket.send(json.dumps(json_data))
    print(f"R: {json_data}")

    answer = await websocket.recv()
    print(f"A: {answer}")


async def test_success_registration():
    async with websockets.connect(host) as websocket:
        await success_register(websocket)


async def test_exists_registration():
    """
    Not used success_register, becouse
    asserts.
    """
    async with websockets.connect(host) as websocket:

        correct_creds = {
            "Type": "account",
            "Command": "registration",
            "Login": "user",
            "Password": "password",
        }

        await websocket.send(json.dumps(correct_creds))
        print(f"R: {correct_creds}")

        answer = await websocket.recv()
        print(f"A: {answer}")

        assert json.loads(answer) == {
            "Type": "account",
            "Command": "registration",
            "Status": "user exist"
        }


async def test_success_sign_in():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

        # await get_requests(websocket)


async def test_failture_sign_in_bad_password():
    async with websockets.connect(host) as websocket:

        await failture_login(websocket)


async def test_failture_sign_in_user_not_exist():
    async with websockets.connect(host) as websocket:

        uncorrect_creds = {
            "Type": "account",
            "Command": "login",
            "Login": "user123",
            "Password": "password123",
        }

        await failture_login(websocket, uncorrect_creds)


async def test_succsses_logout():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await success_logout(websocket)


async def test_failture_logout():
    """
    User not sign in
    """
    async with websockets.connect(host) as websocket:

        await success_logout(websocket, failture=True)


async def test_succsses_create_chat():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await success_create_chat(websocket)


async def test_failed_create_chat():
    """
    User not sign in
    """
    async with websockets.connect(host) as websocket:

        chat_data = {"Type": "chat", "Command": "create", "Chat": "boltaika"}

        await success_create_chat(websocket, chat_data, reson=False)


async def test_success_create_close_chat():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await success_create_close_chat(websocket)


async def test_failed_create_non_auth():
    async with websockets.connect(host) as websocket:

        await success_create_chat(websocket, reson=False)


async def test_success_send_chat_list():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

        await send_chat_list(websocket)


async def test_nonauth_get_chat_list():
    async with websockets.connect(host) as websocket:

        await send_chat_list(websocket)


async def test_success_choise_chat():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

        await choice_chat(websocket)


async def test_success_delete_chat():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)

        chat_data = {
            "Type": "chat",
            # "Command": "choice",
            "Command": "create",
            "Chat": "temp",
        }

        # await choice_chat(websocket, chat_data)
        await success_create_chat(websocket, chat_data)

        await delete_chat(websocket)


async def test_success_delete_close_chat():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)

        chat_data = {
            "Type": "chat",
            # "Command": "choice",
            "Command": "create",
            "Chat": "sec",
            "Password": "sec",
        }

        # await choice_chat(websocket, chat_data)
        await success_create_close_chat(websocket, chat_data)

        await delete_chat(websocket)


async def test_success_enter_in_closed_chat():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        data = {
            "Type": "chat",
            "Command": "choice",
            "Chat": "secret general",
            "Password": "secret"
        }
        await choice_chat(websocket, data=data)


async def test_failed_enter_in_closed_chat():
    """
    Field `Password` not in json request
    """
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

        data = {"Type": "chat", "Command": "choice", "Chat": "secret general"}

        await choice_close_chat(websocket, data)


async def test_failed_enter_in_closed_chat_bad_pass():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

        data = {
            "Type": "chat",
            "Command": "choice",
            "Chat": "secret general",
            "Password": "terces",
        }

        await choice_close_chat(websocket, data)


async def test_success_send_message():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)
        await choice_chat(websocket)
        await send_message(websocket)


async def test_success_send_image():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)
        await choice_chat(websocket)
        await send_image(websocket)


async def test_success_reply_message():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)
        await choice_chat(websocket)

        message_data = {
            "Type": "chat",
            "Command": "message",
            "Text": "Test reply message",
            "Reply": {
                "id": "1",
            }
        }

        await send_message(websocket, message_data)
        await get_requests(websocket)


async def test_success_send_image_and_text():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)
        await choice_chat(websocket)
        message_data = {
            "Type": "chat",
            "Command": "message",
            "Text": "Look! I find new memas",
        }
        await send_image(websocket, message_data=message_data)


async def test_success_send_message_to_closed_chat():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await choice_close_chat(websocket)
        await send_message(websocket)


async def test_success_send_message_next_page():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await choice_chat(websocket)
        await send_message_next_page(websocket)
        await send_message_next_page(websocket)


async def test_failed_send_message_chat_not_exist():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

        data = {"Type": "chat", "Command": "choice", "Chat": "qwerty"}

        await choice_chat(websocket, data)
        await send_message(websocket)


async def test_list_online_users():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await choice_chat(websocket)

        json_data = {"Type": "chat", "Command": "connected"}
        await send_custom_json(websocket, json_data)


async def test_reconnect():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)

    async with websockets.connect(host) as websocket:

        await choice_chat(websocket)
        await send_message(websocket)


async def test_multupule_connection():
    async with websockets.connect(host) as websocket:

        await success_signin(websocket)
        await choice_chat(websocket)
        await send_message(websocket)

    async with websockets.connect(host) as ws:

        register_creds = {
            "Type": "account",
            "Command": "registration",
            "Login": "admin",
            "Password": "admin"
        }

        signin_creds = {
            "Type": "account",
            "Command": "login",
            "Login": "admin",
            "Password": "admin"
        }

        await success_signin(ws, signin_creds)

        chat_data = {
            "Type": "chat",
            "Command": "create",
            "Chat": "genaral",
            # "Chat": "private"
        }

        await choice_chat(ws)

        await asyncio.sleep(2)

        message_data = {
            "Type": "chat",
            "Command": "message",
            "Text": "ADMIN: Hey, there is somebody?",
        }

        await send_message(ws, message_data)


async def test_success_purge_messages():
    async with websockets.connect(host) as websocket:
        await success_signin(websocket)
        await choice_chat(websocket)

        json_data = {"Type": "chat", "Command": "purge"}

        await send_custom_json(websocket, json_data)


async def create_base_for_test():
    await test_success_registration()
    await test_succsses_create_chat()
    await test_success_create_close_chat()


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
        # test_success_delete_chat(),
        # test_success_delete_close_chat(),
        # test_success_send_chat_list(),
        # test_success_enter_in_closed_chat(),
        # test_success_send_message(),
        # test_success_send_message_to_closed_chat(),
        # test_success_send_message_next_page(),
        # test_success_send_image(),
        # test_success_send_image_and_text(),
        # test_success_reply_message(),
        # test_success_purge_messages(),
        # test_failed_enter_in_closed_chat(),
        # test_failed_enter_in_closed_chat_bad_pass(),
        # test_nonauth_get_chat_list(),
        # test_failed_create_non_auth(),
        # test_failed_send_message_chat_not_exist(),
        # test_reconnect(), only for browser
        # test_list_online_users(),
        # test_failed_create_chat(),  # test after realise redirect for non auth
        # test_fault_logout(),# not need becouse, if logout, then logout
        # register test_multupule_connection(),
    ))
