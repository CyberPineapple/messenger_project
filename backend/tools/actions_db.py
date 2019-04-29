from accounts.models import User

async def insert_db_user(manager,**kwargs):
    await manager.create_or_get(User, username=kwargs["Login"],
                                password=kwargs["Password"])


async def extract_db_user(manager,**kwargs):
    try:
        user = await manager.get(User, username=kwargs["Login"])
        return user.username, user.password
    except:
        return False
