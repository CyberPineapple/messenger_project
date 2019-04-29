import peewee

from datetime import datetime

from accounts.models import User
from tools.models import BaseModel


class Chat(BaseModel):
    class Meta:
        db_table = "chats"
        order_by = ("last_send",)

    name = peewee.CharField(max_length=32, unique=True, null=False, index=True)
    date_last_send = peewee.DateTimeField(default=datetime.now())
    owner = peewee.ForeignKeyField(User)

    @classmethod
    async def all_chats(cls, manager):
        return await manager.execute(cls.select())

    async def n_messages(self, manager, num):
        """ Change on return n - messages """
        return await manager.prefetch(self.messages, User.select())


class Message(BaseModel):
    """ Base model for messages """
    class Meta:
        db_table = "messages"
        order_by = ("date_send",)

    user_from = peewee.ForeignKeyField(User, null=True)
    chat = peewee.ForeignKeyField(Chat, related_name="messages")
    text = peewee.TextField()
    date_send = peewee.DateTimeField(default=datetime.now())

    def as_dict(self):
        return {
            "Type": "Message",
            "Text": self.text,
            "From": self.user_from.username,
            "To": self.user_to.username,
            "Date": self.date_send,
        }
