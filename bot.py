import logging
import logging.config
# Credit @ph0enix_web.
# Maintained by @ph0enix_web
# New maintainer @ph0enix_web
# Thank you to the original developer for the base code.
# Credit to the original developer.
# For support, contact @ph0enix_web on Telegram. 
# This is a free and open-source project.
# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from phoenixbot import PhoenixAutofilterBot

from util.keepalive import ping_server
from phoenixbot.clients import initialize_clients


PORT = "8080"
PhoenixAutofilterBot.start()
loop = asyncio.get_event_loop()


async def Phoenix_start():
    print('\n')
    print(' Initalizing Telegram Bot ')
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    bot_info = await PhoenixAutofilterBot.get_me()
    PhoenixAutofilterBot.username = bot_info.username
    await initialize_clients()
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats , lz_verified = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    temp.PHOENIX_VERIFIED_CHATS = lz_verified
    await Media.ensure_indexes()
    me = await PhoenixAutofilterBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    PhoenixAutofilterBot.username = '@' + me.username
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if ON_HEROKU else BIND_ADRESS
    await web.TCPSite(app, bind_address, PORT).start()
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(Phoenix_start())
        logging.info('-----------------------🧐 Service running in Phoenix Mode 😴-----------------------')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')
