from .models import Chat, Message
from tools.sessions import login_required
from aiohttp import web


class ActionChat(web.View):

    @login_required
    async def create_chat(self, **jdata):
        name = jdata["Chat"]
        user = self.request.session.get("user")
        if await self.request.app.manager.count(
            Chat.select().where(Chat.name == name)):
            return {"Type": "chat", "Status": "chat exist"}
        if "Password" in jdata.keys():
            await self.request.app.manager.create(
                Chat, name=name, owner=user,
                password=jdata["Password"], closed=True)
        else:
            await self.request.app.manager.create(Chat, name=name, owner=user)

        self.request.session["chat"] = enter_chat
        return {"Type": "chat", "Status": "success"}

    @login_required
    async def send_chats_users(self):
            # The problem:
            # Func sends only chats created by user
            username = self.request.session.get("user")
            print("From chat/views.py:",username)
            chats = []
            query_chats = await self.request.app.manager.execute(
                Chat.select().where(Chat.owner == username))
            for chat in query_chats:
                chats.append(chat.name)
            return {"Type": "chat", "Chats": chats}

    @login_required
    async def send_messages_from_chat(self, **jdata):
        # user = self.request.session.get("user")
        enter_chat = jdata["Chat"]
        chat = await self.request.app.manager.get(Chat, name=enter_chat)
        if chat.closed and "Password" not in jdata.keys():
            return {"Type":"chat", "Status":"access denied"}
        elif "Password" in jdata.keys():
            if chat.password != jdata["Password"]:
                return {"Type":"chat", "Status":"access denied"}

        self.request.session["chat"] = enter_chat
        query_messages = await self.request.app.manager.execute(
            Message.select().where(Message.chat == enter_chat))
        messages = []
        data_message = {}
        for message in query_messages:
            # The option allow_sync becouse message.user
            # it is foreign key from User db, if del,
            # can use list comphehension.
            with self.request.app.manager.allow_sync():
                data_message["user"] = str(message.user)
                data_message["text"] = message.text
                data_message["date"]= str(message.created_at)
                messages.append(data_message.copy())
        return {"Type":"chat", "Messages": messages}

    @login_required
    async def send_message(self,**jdata):
        chat = self.request.session.get("chat")
        user = self.request.session.get("user")
        if not (chat and user):
            return {"Type":"chat",
                    "Command":"message",
                    "Status":"error in chat or user"}
        await self.request.app.manager.create(
                        Message,
                        user=user,
                        chat=chat,
                        text=jdata["Text"])
        jdata["Status"] = "success"
        for ws in self.request.app.active_sockets:
            await ws.send_json(jdata)

    @login_required
    async def send_list_chats(self):
        return Chat.all_chats()

# class ActionMessages(web.View):

    # @login_required
    # async def broadcast(self, in_chat=False, **jdata):
    #     try:
    #         chat = await self.request.app.manager.get(Chat,
    #                                                   Chat.name ** jdata["Chat"])
    #     except Chat.DoesNotExist:
    #         return {"Type": "chat", "Status": "chat not exist"}
    #     await self.request.app.manager.create(
    #         Message,
    #         # user=self.request.session.get("user"),
    #         user=jdata["User"],
    #         chat=jdata["Chat"],
    #         text=jdata["Text"])
    #     jdata["Status"] = "success"
    #     if in_chat is False:
    #         for ws in self.request.app.active_sockets:
    #             await ws.send_json(jdata)
    #     # else:
        #    for ws in self.request.app.manager.
