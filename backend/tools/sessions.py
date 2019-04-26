from aiohttp_session import get_session
from accounts.models import User

from aiohttp import web


async def request_user_middleware(app, handler):
    print(dir(app))

    async def middleware(request):
        request.session = await get_session(request)
        request.user = None
        user_id = request.session.get('user')
        if user_id is not None:
            request.user = await request.app.objects.get(User, id=user_id)
        return await handler(request)
    return middleware
