from aiohttp_session import get_session
from aiohttp.web import middleware
from accounts.models import User
from chat.models import Chat


@middleware
async def request_user_middleware(request, handler):
    request.session = await get_session(request)
    request.user = None
    request.chat = None

    user_ident = request.session.get("user")
    chat_ident = request.session.get("chat")
    if user_ident is not None:
        request.user = await request.app.manager.get(User,
                                User.username == user_ident)
        if chat_ident is not None:
            request.chat = await request.app.manager.get(Chat,
                                Chat.name == chat_ident)

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
# TASK
# think up container which have
# link like chat -> [user -> ws, ...]
# easy add chat, user and remove them
# where chat, may be is None
#
async def add_active_sockets(request):
    user = request.session.get("user")
    chat = request.session.get("chat")
    ws = request.app.websocket
    active_sockets = request.app.active_sockets

    if chat not in active_sockets.keys():
        active_sockets[chat] = []

    # del user if him in another chat
    # TODO: Del eof session
    for i in active_sockets.items():
        for n, j in enumerate(i[1]):
            if user in j.keys():
                active_sockets[i[0]][n].popitem()

    # and add him in chat
    active_sockets[chat].append({user: ws})
