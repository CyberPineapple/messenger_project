import peewee
from tools import models


class User(models.BaseModel):
    """ Base model for users """

    class Meta:
        db_table = "users"
        order_by = "date_register"

    username = peewee.CharField(max_length=20, unique=True, primary_key=True)
    # password it's sha-1(password + salt)
    password = peewee.CharField(max_length=192)
    online = peewee.BooleanField(default=True)

    # datetime.utcfromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S')
    date_register = peewee.TimestampField()
    date_last_online = peewee.TimestampField()

    def __str__(self):
        return self.username
