import peewee
from accounts.models import User
from tools.models import BaseModel


class Chat(BaseModel):
    class Meta:
        db_table = "chats"
        order_by = ("last_send", )

    # Maybe use `unique` is not true way, becouse
    # if two chats it is name user.
    # or user name = owner+name in db
    name = peewee.CharField(max_length=32, unique=True, primary_key=True)
    owner = peewee.ForeignKeyField(User)
    password = peewee.CharField(max_length=192, null=True)
    closed = peewee.BooleanField(default=False)
    date_last_send = peewee.TimestampField()

    def __str__(self):
        return self.name

    @classmethod
    async def all_chats(cls, manager):
        chats = await manager.execute(cls.select())

        return {
            "Type":
            "chat",
            "Command":
            "list",
            "Chats": [{
                "Chat": chat.name,
                "Closed": chat.closed
            } for chat in chats],
        }


class Message(BaseModel):
    """ Base model for messages """

    class Meta:
        db_table = "messages"
        order_by = ("date_send", )

    user = peewee.ForeignKeyField(User, backref="user_messages")
    chat = peewee.ForeignKeyField(Chat, backref="messages")
    text = peewee.TextField()
    created_at = peewee.TimestampField()
