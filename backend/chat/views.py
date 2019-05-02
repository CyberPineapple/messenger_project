from .models import Chat, Message
from tools.sessions import login_required
from aiohttp import web


class ActionChat(web.View):

    @login_required
    async def create(self, **jdata):
        name = jdata["Chat"]
        user = self.request.session.get("user")
        if await self.request.app.manager.count(Chat.select().where(Chat.name ** name)):
            return {"Type": "chat", "Status": "chat exist"}
        await self.request.app.manager.create(Chat, name=name, owner=user)
        return {"Type": "chat", "Status": "success"}

    async def send_chats_users(self):
        # user? in db or session
        user = self.request.session.get("user")
        chats = []
        query_chats = await self.request.app.manager.execute(Chat.select().where(Chat.owner == user))
        for chat in query_chats:
            chats.append(chat.name)
        return {"Type": "chat", "Chats": chats}


class ActionMessages(web.View):

    @login_required
    async def broadcast(self, in_chat=False, **jdata):
        try:
            chat = await self.request.app.manager.get(Chat,
                                                      Chat.name ** jdata["Chat"])
        except Chat.DoesNotExist:
            return {"Type": "chat", "Status": "chat not exist"}
        await self.request.app.manager.create(
            Message,
            user=self.request.session.get("user"),
            chat=chat,
            text=jdata["Text"])
        jdata["Status"] = "success"
        if in_chat is False:
            for ws in self.request.app.active_sockets:
                await ws.send_json(jdata)
        # else:
        #    for ws in self.request.app.manager.
