from telethon import __version__, events, Button
import asyncio
import sys
import heroku3
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

pongg = "ᴀᴜᴛʜᴏʀ"
PIC = "https://telegra.ph/file/2f2b8d40e3f2fa4acdc8f.mp4"
Alivemsg = "ᴀᴜᴛʜᴏʀ x ꜱᴘᴀᴍ ʜᴇʀᴇ"

TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌=≡❰ • ᴀᴜᴛʜᴏʀ ɪꜱ ᴀʟɪᴠᴇ • ❱≡=\n"
TEXT = f"‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌🚀 ʙᴏᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 🚀\n"
TEXT += f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
TEXT += f"**• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ**🐍: `3.11.3`\n"
TEXT += f"**• ꜱᴘᴀᴍʙᴏᴛ ᴠᴇʀꜱɪᴏɴ**⚙️: `M2.0`\n"
TEXT += f"**• ɢʀᴏᴜᴘ 💫: [ᴅᴇᴠɪʟ ᴄʜᴀᴛᴢ 🥀](https://t.me/DEVIL_CHATZ)**\n"
TEXT += f"**• ᴄʜᴀɴɴᴇʟ ✨: [ᴅᴇᴠɪʟ ᴛᴇᴄʜ 🥀](https://t.me/+XxS3X3ayLqQ5Njdk)**\n"
TEXT += f"**• ᴅᴇᴠ 🫂: [Dᴇᴠɪʟ 🥀](https://t.me/kexx_XD)**\n"
TEXT += f"➖➖➖➖➖➖➖➖➖➖➖➖"
                                  
@X1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  PIC,
                                  caption=TEXT,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/rasedidstore"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/+dKGCo7oumwYwZDNl")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
