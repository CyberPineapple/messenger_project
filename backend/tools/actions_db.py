from accounts.models import User

async def insert_db_user(objects,**kwargs):
    await objects.create_or_get(User, username=kwargs["Login"],
                                password=kwargs["Password"])


async def extract_db_user(objects,**kwargs):
    try:
        user = await objects.get(User, username=kwargs["Login"])
        return user.username, user.password
    except:
        return False
