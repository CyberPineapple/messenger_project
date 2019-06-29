import imghdr
import uuid
import os
import base64


async def is_image(str_base64):
    binary = base64.b64decode(str_base64[:str_base64.index(",") + 1])
    path = f"/tmp/{uuid.uuid1()}"
    flag = False
    with open(path, "wb") as tmpfile:
        tmpfile.write(binary)
        if imghdr.what(path):
            flag = True
    os.remove(path)
    return flag
