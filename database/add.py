# with Love @ph0enix_web 💘
# Subscribe YT @ph0enix_web - to learn more about this for free...

from database.users_chats_db import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        print("user added to db")
    else:
        print("user already in db")

        


