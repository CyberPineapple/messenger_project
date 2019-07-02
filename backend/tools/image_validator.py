import imghdr
import uuid
import os
import base64
from time import time


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


async def store_image(str_base64, chat):
    local_path = f'./../../public/images/{chat}/'
    if not os.path.isdir(local_path):
        os.mkdir(local_path)  # descriptors
    cuted_base64 = base64.b64decode(str_base64[str_base64.index(",") + 1:])
    unix_time = str(int(time()))
    local_path = local_path + unix_time
    with open(local_path, 'wb') as image:
        image.write(cuted_base64)
    # TODO: send full path to image
    path = '/images/' + chat + "/" + unix_time + "." + str_base64[11:14]
    return path
