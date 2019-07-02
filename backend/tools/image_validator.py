import imghdr
import uuid
import os
import base64


async def is_image(str_base64):
    flag = False
    if str_base64 == []:
        return flag
    cuted_base64 = base64.b64decode(str_base64[str_base64.index(",") + 1:])
    path = f"/tmp/{uuid.uuid1()}"
    with open(path, "wb") as tmpfile:
        tmpfile.write(cuted_base64)
        if imghdr.what(path):
            flag = True
    os.remove(path)
    return flag
