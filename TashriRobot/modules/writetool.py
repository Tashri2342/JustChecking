import subprocess
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from TashriRobot import BOT_NAME, BOT_USERNAME
from TashriRobot import pbot as Tashri


@Tashri.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
    else:
        text = message.reply_to_message.text

    m = await Tashri.send_message(
        message.chat.id, "`Please wait...,\n\nWriting your text...`"
    )

    cmd = f'curl -X GET "https://api.safone.me/write?text={text}" -H "accept: application/json"'
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        req = result.stdout.strip()
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
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )
    else:
        await m.edit("An error occurred while processing the request.")


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__help__ = """
 ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.

☆............𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆
"""
