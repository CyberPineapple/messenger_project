from aiohttp_session import get_session
from accounts.models import User

from aiohttp import web


async def request_user_middleware(app, handler):
    async def middleware(request):
        session = await get_session(request)
        #request.session = await get_session(request)
        request.user = None
        user_id = session.get('user')
        if user_id is not None:
            request.user = await request.app.manager.get(User, id=user_id)
        return await handler(request)
    return middleware


def login_required(func):
    """ Allow only auth users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is None:
            print("login_required: Logout")
            # redirect(self.request, 'login')
        return await func(self, *args, **kwargs)
    return wrapped

def anonymous_required(func):
    """ Allow only anonymous users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is not None:
            print("Login please.")
            #redirect(self.request, 'index')
        return await func(self, *args, **kwargs)
    return wrapped
