from aiohttp import web
from time import time

from .models import User
from tools.passwords import hash_password, verify_password
from tools.sessions import login_required, anonymous_required
from aiohttp_session import get_session


class LogIn(web.View):

    async def _login_user(self, user):
        """ Create session for user  """
        self.request.session["user"] = str(user.username)
        self.request.session["time"] = time()



    @anonymous_required
    async def loginning(self, **kwargs):
        """ Check username and password  """
        username = kwargs["Login"]
        password = kwargs["Password"]

        try:
            user = await self.request.app.manager.get(
                            User, User.username ** username)
            if verify_password(user.password, password):
                await self._login_user(user)
                return {"Type": "login", "Status": "success"}
            raise User.DoesNotExist
        except User.DoesNotExist:
            return {"Type": "login", "Status": "error"}


class Register(LogIn):

    @anonymous_required
    async def create_user(self, **kwargs):
        """ Insert into db user """

        username = kwargs["Login"]
        password = hash_password(kwargs["Password"])

        if await self.request.app.manager.count(
            User.select().where(User.username == username)):
            return {"Type": "registration", "Status": "user exist"}

        user = await self.request.app.manager.create(
            User, username=username, password=password,)
        await self._login_user(user)
        return {"Type": "registration", "Status": "success"}


class LogOut(web.View):

    @login_required
    async def logout(self):
        """ Remove user from session """
        try:
            self.request.session.pop("user")
            return {"Type": "logout", "Status": "success"}
        except KeyError:
            return {"Type": "logout", "Status": "error"}
