from aiohttp import web
from time import time

from .models import User
from tools.passwords import hash_password, verify_password


class LogIn(web.View):

    async def login_user(self, user):
        self.request.session["user"] = str(user.id)
        self.requets.session["time"] = time()

    async def loginning(self, **kwargs):
        username = kwargs["Login"]
        password = kwargs["Password"]

        try:
            user = await self.request.app.objects.get(User, User.username ** username)
            if verify_password(user.password, password):
                await self.login_user(user)
                return True
        except User.DoesNotExist:
            return False



class Register(LogIn):

    async def create_user(self, **kwargs):
        username = kwargs["Login"]
        password = hash_password(kwargs["Password"])

        if await self.request.app.objects.count(User.select().where(User.username ** username)):
            return False
        user = await self.request.app.objects.create(User, username=username,
                                                           password=password,)
        await self.login_user(user)
        return True

class LogOut(web.View):
    pass
