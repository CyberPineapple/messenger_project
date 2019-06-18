import imghdr
import uuid
import os

# from tools.sessions import login_required


# @login_required
# TODO: security problem
# anyone send to server binary image
async def is_image(binary):
    path = f"/tmp/{uuid.uuid1()}"
    flag = False
    with open(path, "wb") as tmpfile:
        tmpfile.write(binary)
        if imghdr.what(path):
            flag = True
    os.remove(path)
    return flag
