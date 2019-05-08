from aiohttp_session import get_session
from aiohttp.web import middleware
from accounts.models import User


@middleware
async def request_user_middleware(request, handler):
    request.session = await get_session(request)
    request.user = None
    user_ident = request.session.get('user')
    if user_ident is not None:
        request.user = await request.app.manager.get(
                                User.username == user_ident)
    responce = await handler(request)
    print(request.user)
    return responce


#async def request_user_middleware(app, handler):
#    async def middleware(request):
#        request.session = await get_session(request)  # send the session
#        user_ident = request.session.get('user')  # find in store
#        if user_ident is not None:  # if find get him
#            print("WARNING!!")
#            request.user = await request.app.manager.get(
#                User.username == user_ident)
#
#        request.user = None  # init state
#        print("From tools/session:", request.user, user_ident)
#
#        return await handler(request)
#    return middleware


def login_required(func):
    """ Allow only auth users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is None:
            # TODO exit non login user
            print("login_required: Logout")
            # redirect(self.request, 'login')
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
