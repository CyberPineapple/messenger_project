from datetime import datetime

import peewee

from tools import models


class User(models.BaseModel):
    """ Base model for users """
    class Meta:
        db_table = "users"
        order_by = ("date_register")

    id = peewee.AutoField(null=False)
    username = peewee.CharField(max_length=20, unique=True)
    # password = sha-1(name+password)
    password = peewee.CharField(max_length=64)
    online = peewee.BooleanField(default=True)

    date_register = peewee.DateTimeField(default=datetime.now())
    date_last_online = peewee.DateTimeField(default=datetime.now())
