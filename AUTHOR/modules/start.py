from telethon import __version__, events
from pyrogram.types import InlineKeyboardButton
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        InlineKeyboardButton(
            text="ᴀᴜᴛʜᴏʀ 🥀", url="https://t.me/Kexx_XD"
        ),
        InlineKeyboardButton(
            text="ꜱᴜᴘᴘᴏʀᴛ ✨", url="https://t.me/DEVIL_CHATZ"
        ),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🧸",
            url="https://t.me/{x.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ❄️", url="https://t.me/+dKGCo7oumwYwZDNl"
        ),
        InlineKeyboardButton(
            text="ᴄʜᴀɴɴᴇʟ ☁️", url="https://t.me/+XxS3X3ayLqQ5Njdk"
        ),
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ 🥀{event.sender.first_name}❤️\n\n╔═════════════════╗\n║ ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​** ║\n"
        TEXT += f"║═════════════════║\n"       
        TEXT += f"║» **ᴅᴇᴠ​ 🫂: [⏤͟͞〲ᴅᴇᴠɪʟ](https://t.me/KANU_XD)** ║\n"
        TEXT += f"║» **ᴅᴇᴠɪʟ ⚙️:** `1.0` ║\n"
        TEXT += f"║» **ᴘʏᴛʜᴏɴ 🐍:** `3.11` ║\n"
        TEXT += f"║» **ᴛᴇʟᴇᴛʜᴏɴ 🔰:** `{__version__}` ║\n╚═════════════════╝"
        await event.client.send_file(
            event.chat_id,
            "https://graph.org/file/83433ce8aa8af96f47cb3.jpg",
            caption=TEXT,
            buttons=START_OP
        )
