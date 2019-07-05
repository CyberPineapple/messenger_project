from aiohttp import web
from tools.image_validator import is_image, store_image
from tools.passwords import hash_password, verify_password
from tools.sessions import add_active_sockets, create_instance, login_required

from .models import Chat, Message


class ActionChat(web.View):

    limiter = 30

    @staticmethod
    async def send_messages(instance, manager, chat=None, command="choice"):
        data = {"Type": "chat", "Command": command}
        if chat is not None:
            data["Chat"] = chat
        messages = []
        data_message = {}

        for message in instance:
            # The option allow_sync becouse message.user
            # it is foreign key from User db, if del,
            # can use list comphehension.
            with manager.allow_sync():

                data_message["user"] = str(message.user)
                data_message["date"] = str(message.created_at)

                if message.text is not None:
                    data_message["text"] = message.text

                if message.image is not None:
                    data_message["image"] = message.image

                messages.append(data_message.copy())
                data_message.clear()

        data["Messages"] = messages[::-1]
        return data

    @login_required
    async def create_chat(self, **jdata):
        chat = jdata["Chat"]
        user = self.request.session.get("user")

        if await self.request.app.manager.count(
                Chat.select().where(Chat.name == chat)):

            return {"Type": "chat", "Status": "chat exist"}

        if "Password" in jdata.keys():
            password = hash_password(jdata["Password"], algorithm="sha256")
            await self.request.app.manager.create(Chat,
                                                  name=chat,
                                                  owner=user,
                                                  password=password,
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
        jchat = jdata.get("Chat", None)
        manager = self.request.app.manager
        try:
            chat = await manager.get(Chat, name=jchat)
        except Chat.DoesNotExist:
            return {"Type": "chat", "Status": "error"}

        if chat.closed and "Password" not in jdata.keys():
            return {"Type": "chat", "Status": "access denied"}
        elif "Password" in jdata.keys():
            if not verify_password(
                    chat.password, jdata["Password"], algorithm="sha256"):

                return {"Type": "chat", "Status": "access denied"}

        self.request.session["chat"] = jchat
        await create_instance(self.request)
        await add_active_sockets(self.request)

        self.request.session["page"] = 1
        page = self.request.session.get("page")

        chat_messages = await manager.execute(
            self.request.chat.messages.order_by(-Message.created_at).paginate(
                page, self.limiter))

        return await ActionChat.send_messages(chat_messages, manager, jchat)

    @login_required
    async def send_message(self, **jdata):
        chat = self.request.session.get("chat")
        user = self.request.session.get("user")
        path_to_image = None
        text = None

        if not (chat and user):
            return {
                "Type": "chat",
                "Command": "message",
                "Status": "error in chat or user",
            }

        answer = {
            "Type": "chat",
            "Command": "message",
            "Message": {
                "user": user
            }
        }

        if "Text" in jdata.keys():
            text = jdata["Text"]
            answer["Message"]["text"] = text

        if "Image" in jdata.keys():
            image = jdata["Image"]
            ext = await is_image(image)
            if not ext:
                return {
                    "Type": "chat",
                    "Command": "message",
                    "Status": "failed to attach image",
                }
            path_to_image = await store_image(
                image,
                ext,
                chat,
            )

            answer["Message"]["image"] = path_to_image
        await self.request.app.manager.create(Message,
                                              user=user,
                                              chat=chat,
                                              image=path_to_image,
                                              text=text)

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

            for ws in self.request.app.active_sockets.get_chat(
                    self.request.session["chat"]).all_ws():
                await ws.send_json(
                    await self.send_messages_from_chat(**{"Chat": "general"}))
                # There maybe bug, as in send_messages_from_chat
                # `request.chat = 'general'`
                # but after self.request.chat = None(next strings)
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

    async def send_list_online_users(self):
        chat = self.request.session.get("chat")
        users = self.request.app.active_sockets.get_chat(chat).all_users()
        return {"Type": "chat", "Command": "connected", "Online": users}

    # temp functionality
    @login_required
    async def purge_messages(self):
        chat = self.request.session.get("chat")

        if not chat:
            return {
                "Type": "chat",
                "Command": "purge",
                "Status": "purge is not completed",
            }

        await self.request.app.manager.execute(
            Message().delete().where(Message.chat_id == chat))
        return {"Type": "chat", "Command": "purge", "Status": "Success"}
