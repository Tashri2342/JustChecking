from TashriRobot import pbot
import os
import emoji
import re
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
import regex

def remove_emoji(string):
    return regex.sub(r'\p{Emoji}', '', string)

@pbot.on_message(filters.command("fnews"))
async def fake_news(client, message):
    # The code for the fake_news function remains unchanged.

@pbot.on_message(filters.command("ph"))
async def fake_comment(client, message):
    dl = "ph_comment.jpg"
    args = message.command[1]
    if not args:
        await message.reply("gib sum temxt 🌚")
        return

    args = str(remove_emoji(args))
    eris = await message.reply("🌚")
    me = await pbot.get_me()
    u = me.username if me.username else me.first_name

    if message.reply_to_message:
        r = message.reply_to_message
        u = r.from_user.username if r.from_user.username else r.from_user.first_name

    if not os.path.exists("ph_font.TTF"):
        await pbot.download_media(
            await pbot.get_messages("e3ris_db", ids=5903)
        )

    if not os.path.exists(dl):
        get = await pbot.get_messages("e3ris_db", ids=5909)
        dl = await get.download_media()

    img = Image.open(dl)
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("ph_font.TTF", 100)
    d1.text((385, 640), u, font=myFont, fill=(135, 98, 87))
    d1.text((76, 960), args, font=myFont, fill=(203, 202, 202))
    img.save("pphh.jpg")
    img = "pphh.jpg"

    await pbot.send_photo(
        message.chat.id,
        await pbot.upload_photo(img),
        reply_to_message_id=message.reply_to_message.message_id,
        force_document=False,
    )

    os.remove(img)
    await eris.delete()

__mod_name__ = "Pornhub Fake"

__help__ = """
✘ **Commands Available :**
> `{i}ph <some_text>`
> `{i}fnews <text> <reply to a picture>`

☆............𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆
"""
