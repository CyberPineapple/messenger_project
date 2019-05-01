import peewee

from accounts.models import User
from tools.models import BaseModel


class Chat(BaseModel):
    class Meta:
        db_table = "chats"
        order_by = ("last_send",)

    name = peewee.CharField(max_length=32, unique=True)
    owner = peewee.ForeignKeyField(User)
    date_last_send = peewee.TimestampField()

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

    user = peewee.ForeignKeyField(User, backref='messages')
    chat = peewee.ForeignKeyField(Chat)
    text = peewee.TextField()
    created_at = peewee.TimestampField()
