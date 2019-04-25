import peewee

from datetime import datetime
from peewee_async import PostgresqlDatabase



database = PostgresqlDatabase(None)

class User(peewee.Model):
    """ Base model for users """
    class Meta:
        database = database
        db_table = "users"
        order_by = ("date_register")

    id = peewee.PrimaryKeyField(null=False)
    username = peewee.CharField(max_length=40, unique=True)
    # password = sha-1(name+password)
    password = peewee.CharField(max_length=44)  # len for sha-1
    online = peewee.BooleanField(default=True)

    date_register = peewee.DateTimeField(default=datetime.now())
    date_last_online = peewee.DateTimeField(default=datetime.now())


# class Chat(peewee.Model):
#     class Meta:
#         database = database
#         db_table = "messages"
#
#     name_chat = peewee.CharField(max_lenght=100)

class Message(peewee.Model):#, Chat):
    """ Base model for messages """
    class Meta:
        database = database
        order_by = ("date_send",)

    user_from = peewee.CharField(max_length=40)
    user_to = peewee.CharField(max_length=40)
    date_send = peewee.DateTimeField(default=datetime.now())


async def insert_db_user(objects,**kwargs):
    await objects.create_or_get(User, username=kwargs["Login"],
                                password=kwargs["Password"])


async def extract_db_user(objects,**kwargs):
    try:
        user = await objects.get(User, username=kwargs["Login"])
        return user.username, user.password
    except:
        return False
