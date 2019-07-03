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
    binary = base64.b64decode(str_base64[str_base64.index(",") + 1:])
    name_file = str(int(time()))
    local_path = local_path + name_file
    extension = "." + imghdr.what(local_path)
    local_path = local_path + extension
    with open(local_path, 'wb') as image:
        image.write(binary)
    # TODO: send full path to image
    path = '/images/' + chat + "/" + name_file + extension
    return path
