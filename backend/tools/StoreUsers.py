from dataclasses import dataclass, field
from aiohttp.web import WebSocketResponse


@dataclass
class OnlineUser():
    name: str
    ws: WebSocketResponse


@dataclass
class ActiveChat():
    name: str
    pool: list = field(default_factory=list)

    def all_users(self):
        return [user.name for user in self.pool]

    def add_new_user(self, user: OnlineUser):
        if user.name not in self.all_users():
            self.pool.append(user)

    def del_user(self, duser: str):
        for user in self.pool:
            if user.name == duser:
                self.pool.remove(user)

    def remove_all_users(self):
        for user in self.all_users():
            self.del_user(user)

    def get_user(self, fuser: str):
        for user in self.all_users():
            if user == fuser:
                return user

    def all_ws(self):
        return [user.ws for user in self.pool]


@dataclass
class StoreActiveChats():
    pool = []

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(StoreActiveChats, cls).__new__(cls)
        return cls.instance

    def all_chats(self):
        return [chat for chat in self.pool]

    def add_new_chat(self, chat: ActiveChat):
        if chat.name not in self.all_chats():
            self.pool.append(chat)

    def get_chat(self, chat_name: str):
        for chat in self.pool:
            if chat.name == chat_name:
                return chat

    def del_chat(self, chat: str):
        chat = self.get_chat(chat)
        if chat is not None:
            chat.remove_all_users()
            self.pool.remove(chat)

# user = OnlineUser("user", "..")
# user1 = OnlineUser("user", "...")
# login = OnlineUser("login", "....")
# admin = OnlineUser("admin", ",,,")
#
# general = ActiveChat("general")
# poc = ActiveChat("poc")
#
# general.add_new_user(user)
# assert general.all_users() == ['user']
# assert poc.all_users() == []
# general.add_new_user(user1)
# assert general.all_users() == ['user']
# general.add_new_user(login)
# assert general.all_users() == ['user', 'login']
# general.del_user("user")
# assert general.all_users() == ['login']
# poc.add_new_user(admin)
# assert poc.all_users() == ['admin']
# general.remove_all_users()
# assert general.all_users() == []
#
# socket = StoreActiveChats()
# socket.add_new_chat(general)
# assert socket.all_chats() == [ActiveChat(name='general', pool=[])]
# socket.add_new_chat(poc)
# assert socket.all_chats() == [
#     ActiveChat(
#         name='general', pool=[]), ActiveChat(
#             name='poc', pool=[
#                 OnlineUser(
#                     name='admin', ws=',,,')])]
# socket.del_chat("poc")
# assert socket.all_chats() == [ActiveChat(name='general', pool=[])]
