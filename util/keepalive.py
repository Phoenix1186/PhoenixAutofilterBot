# Credit @ph0enix_web.
# Maintained by @ph0enix_web
# New maintainer @ph0enix_web
# Thank you to the original developer for the base code.
# Credit to the original developer.
# For support, contact @ph0enix_web on Telegram. 
# This is a free and open-source project.
import asyncio
import logging
import aiohttp
import traceback
from info import *


async def ping_server():
    sleep_time = PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()
