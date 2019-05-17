from aiohttp_session import get_session

from aiohttp.web import middleware
from accounts.models import User
from chat.models import Chat
from .store_users import OnlineUser, ActiveChat


@middleware
async def request_user_middleware(request, handler):
    request.session = await get_session(request)
    request.user = None
    request.chat = None

    user_ident = request.session.get("user")
    chat_ident = request.session.get("chat")
    if user_ident is not None:
        request.user = \
                await request.app.manager.get(
                    User, User.username == user_ident)
        if chat_ident is not None:
            request.chat = \
                await request.app.manager.get(Chat, Chat.name == chat_ident)

    responce = await handler(request)
    return responce


def login_required(func):
    """ Allow only auth users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is None:
            await self.request.app.websocket.send_json(
                {"Type": "login",
                 "Status": "error"
                 }
            )
            await self.request.app.websocket.close()
        else:
            return await func(self, *args, **kwargs)
    return wrapped


def anonymous_required(func):
    """ Allow only anonymous users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is not None:
            print("Login please.")
            # redirect(self.request, 'index')
        return await func(self, *args, **kwargs)
    return wrapped


async def create_instance(request):
    user_ident = request.session.get("user")
    request.user = await request.app.manager.get(User,
                                                 User.username == user_ident)
    chat_ident = request.session.get("chat")
    if chat_ident is not None:
        request.chat = await request.app.manager.get(Chat,
                                                     Chat.name == chat_ident)


async def add_active_sockets(request):
    ws = request.app.websocket
    active_sockets = request.app.active_sockets

    chat = ActiveChat(request.session.get("chat"))
    user = OnlineUser(request.session.get("user"), ws)

    if chat.name not in active_sockets.all_chat_names():
        active_sockets.add_new_chat(chat)

    # Maybe set var old_chat without
    # iter by all chat.

    # Del user if he in another chat
    for cht in active_sockets.all_chats():
        if cht.get_user(user.name):
            cht.del_user(user.name)

    # and add him in chat
    active_sockets.get_chat(chat.name).add_new_user(user)
