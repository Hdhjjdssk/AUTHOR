import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime
import asyncio

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sgm(?: |$)(.*)" % hl))
async def gm(e):
    if e.sender_id in SUDO_USERS:
        altron = await e.reply(f"🌞")
        await altron.edit(f"╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯.\n\n╱╱╱╱╱╱╱╱╱╱╭╮\n╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sgn(?: |$)(.*)" % hl))
async def gm(e):
    if e.sender_id in SUDO_USERS:
        altron = await e.reply(f"☀️")
        await altron.edit(f"╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n╭━━━━╮\n┃╭╮╭╮┃\n╰╯┃┃╰╯\n╱╱┃┃\n╱╱┃┃\n╱╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭╮╭╯\n┃┃┃╰╮\n╰╯╰━╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃┃╱┃┃\n┃╰━╯┃\n╰━━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃┃╱┃┃\n┃╰━╯┃\n╰━━━╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sga(?: |$)(.*)" % hl))
async def gm(e):
    if e.sender_id in SUDO_USERS:
        altron = await e.reply(f"🌚")
        await altron.edit(f"╭━━━╮╱╱╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╱╱╱┃┃\n┃┃╱╰╋━━┳━━┳━╯┃\n┃┃╭━┫╭╮┃╭╮┃╭╮┃\n┃╰┻━┃╰╯┃╰╯┃╰╯┃\n╰━━━┻━━┻━━┻━━╯\n╭━╮╱╭╮╱╱╱╭╮╱╭╮\n┃┃╰╮┃┃╱╱╱┃┃╭╯╰╮\n┃╭╮╰╯┣┳━━┫╰┻╮╭╯\n┃┃╰╮┃┣┫╭╮┃╭╮┃┃\n┃┃╱┃┃┃┃╰╯┃┃┃┃╰╮\n╰╯╱╰━┻┻━╮┣╯╰┻━╯\n╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╰━━╯")
