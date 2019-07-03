from base64 import b64decode
from hashlib import md5
from uuid import uuid1
import imghdr
import os


async def decoCut_base64(str_base64):
    return b64decode(str_base64[str_base64.index(",") + 1:])


async def is_image(str_base64):
    # possible optimisation -- module tempfile
    if str_base64 == []:
        return None
    path = f"/tmp/{uuid1()}"
    binary = await decoCut_base64(str_base64)
    with open(path, "wb") as tmpfile:
        tmpfile.write(binary)
    extension = imghdr.what(path)
    os.remove(path)
    return extension


async def store_image(str_base64, extension, chat):
    local_path = f'./../../public/images/{chat}/'

    if not os.path.isdir(local_path):
        os.mkdir(local_path, mode=755)

    binary = await decoCut_base64(str_base64)
    name_file = md5(binary).hexdigest()
    name_file_with_extention = name_file + "." + extension
    full_local_path = local_path + name_file_with_extention

    if not os.path.isfile(full_local_path):
        with open(full_local_path, 'wb') as image:
            image.write(binary)

    path = '/images/' + chat + "/" + name_file_with_extention
    return path
