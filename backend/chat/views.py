from aiohttp import web
from tools.sessions import add_active_sockets, create_instance, login_required

from .models import Chat, Message


class ActionChat(web.View):

    limiter = 30

    @staticmethod
    async def send_messages(instance, manager, command="choice"):
        messages = []
        data_message = {}

        for message in instance:
            # The option allow_sync becouse message.user
            # it is foreign key from User db, if del,
            # can use list comphehension.
            with manager.allow_sync():
                data_message["user"] = str(message.user)
                data_message["text"] = message.text
                data_message["date"] = str(message.created_at)
                messages.append(data_message.copy())

        return {"Type": "chat", "Command": command, "Messages": messages[::-1]}

    @login_required
    async def create_chat(self, **jdata):
        chat = jdata["Chat"]
        user = self.request.session.get("user")

        if await self.request.app.manager.count(
                Chat.select().where(Chat.name == chat)):

            return {"Type": "chat", "Status": "chat exist"}

        if "Password" in jdata.keys():
            await self.request.app.manager.create(Chat,
                                                  name=chat,
                                                  owner=user,
                                                  password=jdata["Password"],
                                                  closed=True)
        else:
            await self.request.app.manager.create(Chat, name=chat, owner=user)

        self.request.session["chat"] = chat
        await create_instance(self.request)
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
        jchat = jdata.get("Chat", "general")
        manager = self.request.app.manager
        try:
            chat = await manager.get(Chat, name=jchat)
        except Chat.DoesNotExist:
            return {"Type": "chat", "Status": "error"}

        if chat.closed and "Password" not in jdata.keys():
            return {"Type": "chat", "Status": "access denied"}
        elif "Password" in jdata.keys():
            if chat.password != jdata["Password"]:
                return {"Type": "chat", "Status": "access denied"}

        self.request.session["chat"] = jchat
        await create_instance(self.request)
        await add_active_sockets(self.request)

        self.request.session["page"] = 1
        page = self.request.session.get("page")

        chat_messages = await manager.execute(
            self.request.chat.messages.order_by(-Message.created_at).paginate(
                page, self.limiter))

        return await ActionChat.send_messages(chat_messages, manager)

    @login_required
    async def send_message(self, **jdata):
        chat = self.request.session.get("chat")
        user = self.request.session.get("user")

        if not (chat and user):
            return {
                "Type": "chat",
                "Command": "message",
                "Status": "error in chat or user",
            }
        await self.request.app.manager.create(Message,
                                              user=user,
                                              chat=chat,
                                              text=jdata["Text"])
        answer = {
            "Type": "chat",
            "Command": "message",
            "Message": {
                "user": user,
                "text": jdata["Text"]
            },
        }

        for ws in self.request.app.active_sockets.get_chat(chat).all_ws():
            await ws.send_json(answer)

    @login_required
    async def send_list_chats(self):
        return await Chat.all_chats(self.request.app.manager)

    @login_required
    async def delete_chat(self):
        """
        Assert chat is choised!
        """
        # TODO kick users from deleted chat
        with self.request.app.manager.allow_sync():
            if self.request.user != self.request.chat.owner:
                return {"Type": "chat", "Command": "delete", "Status": "error"}

            self.request.chat.delete_instance(recursive=True)
        self.request.chat = None
        self.request.session["chat"] = None

        return {"Type": "chat", "Command": "delete", "Status": "success"}

    @login_required
    async def earlier_messages(self):
        manager = self.request.app.manager
        page = self.request.session.get("page") + 1
        self.request.session["page"] = page

        chat_messages = await manager.execute(
            self.request.chat.messages.order_by(-Message.created_at).paginate(
                page, self.limiter // 2))

        return await ActionChat.send_messages(chat_messages,
                                              manager,
                                              command="earlier")
