import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from TashriRobot import BOT_NAME, BOT_USERNAME
from TashriRobot import pbot as Tashri

@Tashri.on_message(filters.command("write") & filters.chat_type.groups)
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
    else:
        text = message.reply_to_message.text
        
    m = await Tashri.send_message(
        message.chat.id, "`Please wait...,\n\nWriting your text...`"
    )
    
    API = f"https://api.safone.me/write?text={text}"
    response = requests.get(API)
    
    if response.status_code == 200:
        req = response.url
        caption = f"""
        sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

        ✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
        🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
        ❄ **ʟɪɴᴋ :** `{req}`
        """
        await m.delete()
        await Tashri.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🍁ᴛᴇʟᴇɢʀᴀᴩʜ🍁", url=req)]]
            ),
        )
    else:
        await m.edit("`Error occurred while generating the image.`")

__mod_name__ = "⚡WʀɪᴛᴇTᴏᴏʟ⚡"

__help__ = """

ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.

☆............𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆
"""
