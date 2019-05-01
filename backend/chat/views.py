from .models import Chat, Message
from tools.sessions import login_required
from aiohttp import web


class CreateChat(web.View):

    @login_required
    async def create(self, **jdata):
        name = jdata["Chat"]
        user = self.request.session.get("user")
        if await self.request.app.manager.count(Chat.select().where(Chat.name ** name)):
            return {"Type": "chat", "Status": "chat exist"}
        await self.request.app.manager.create(Chat, name=name, owner=user)
        return {"Type": "chat", "Status": "success"}


class ActionMessages(web.View):

    @login_required
    async def broadcast(self, **jdata):
        try:
            chat = await self.request.app.manager.get(Chat, Chat.name ** jdata["Chat"])
        except Chat.DoesNotExist:
            return {"Type":"chat", "Status":"chat not exist"}
        await self.request.app.manager.create(
            Message,
            user=self.request.session.get("user"),
            chat=chat,
            text=jdata["Text"])
        jdata["Status"] = "success"
        for ws in self.request.app.active_sockets:
            await ws.send_json(jdata)
