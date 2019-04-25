from aiohttp_session import get_session
from accounts.models import User

from aiohttp import web


async def request_user_middleware(app, handler):

    async def middleware(request):
        request.session = await get_session(request)
        request.user = None
        user_id = request.session.get('user')
        if user_id is not None:
            request.user = await request.app.objects.get(User, id=user_id)
        return await handler(request)
    return middleware


def redirect(request, router_name, *, permanent=False, **kwargs):
    """ Redirect to given URL name """
    url = request.app.router[router_name].url(**kwargs)
    if permanent:
        raise web.HTTPMovedPermanently(url)
    raise web.HTTPFound(url)


# def add_message(request, kind, message):
#    """ Put message into session """
#    messages = request.session.get('messages', [])
#    messages.append((kind, message))
#request.session['messages'] = messages

def login_required(func):
    """ Allow only auth users """
    async def wrapped(self, *args, **kwargs):
        if self.request.user is None:
            #add_message(self.request, 'info', 'LogIn to continue.')
            redirect(self.request, 'login')
        return await func(self, *args, **kwargs)
    return wrapped
