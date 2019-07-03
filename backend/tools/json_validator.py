from json import loads


async def is_json(myjson):
    try:
        loads(myjson)
    except ValueError:
        return False

    return True
