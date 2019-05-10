from .models import Chat, Message
from tools.sessions import login_required, add_active_sockets
from aiohttp import web
from datetime import datetime


class ActionChat(web.View):

    @login_required
    async def create_chat(self, **jdata):
        chat = jdata["Chat"]
        user = self.request.session.get("user")
        if await self.request.app.manager.count(
                Chat.select().where(Chat.name == chat)):
            return {"Type": "chat", "Status": "chat exist"}
        if "Password" in jdata.keys():
            await self.request.app.manager.create(
                Chat, name=chat, owner=user,
                password=jdata["Password"], closed=True)
        else:
            await self.request.app.manager.create(Chat, name=chat, owner=user)

        self.request.session["chat"] = chat
        await add_active_sockets(self.request)

        return {"Type": "chat", "Status": "success"}

    @login_required
    async def send_chats_users(self):
        """ Func sends only chats created by user """
        username = self.request.session.get("user")
        chats = []
        query_chats = await self.request.app.manager.execute(
            Chat.select().where(Chat.owner == username))
        for chat in query_chats:
            chats.append(chat.name)
        return {"Type": "chat", "Chats": chats}

    @login_required
    async def send_messages_from_chat(self, **jdata):
        chat = jdata["Chat"]
        chat = await self.request.app.manager.get(Chat, name=chat)
        if chat.closed and "Password" not in jdata.keys():
            return {"Type": "chat", "Status": "access denied"}
        elif "Password" in jdata.keys():
            if chat.password != jdata["Password"]:
                return {"Type": "chat", "Status": "access denied"}

        self.request.session["chat"] = chat
        await add_active_sockets(self.request)
        query_messages = await self.request.app.manager.execute(
            Message.select().where(Message.chat == chat))
        messages = []
        data_message = {}
        for message in query_messages:
            # The option allow_sync becouse message.user
            # it is foreign key from User db, if del,
            # can use list comphehension.
            with self.request.app.manager.allow_sync():
                data_message["user"] = str(message.user)
                data_message["text"] = message.text
                data_message["date"] = str(message.created_at)
                messages.append(data_message.copy())
        return {"Type": "chat", "Messages": messages}

    @login_required
    async def send_message(self, **jdata):
        chat = self.request.session.get("chat")
        user = self.request.session.get("user")
        if not (chat and user):
            return {"Type": "chat",
                    "Command": "message",
                    "Status": "error in chat or user"}
        await self.request.app.manager.create(
                        Message,
                        user=user,
                        chat=chat,
                        text=jdata["Text"])
        jdata["Time"] = datetime.now().isoformat()
        print(dir(chat), chat)
        for user in self.request.app.active_sockets[chat]:
            for ws in user.values():
                await ws.send_json(jdata)

    @login_required
    async def send_list_chats(self):
        return await Chat.all_chats(self.request.app.manager)
