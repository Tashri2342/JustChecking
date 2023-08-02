from TashriRobot import pbot
import os
import emoji
import re
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters

def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)

@pbot.on_message(filters.command("fnews"))
async def fake_news(client, message):
    if message.reply_to_message and message.reply_to_message.media:
        error_ = "Reply to Sticker or Photo"
        args = message.command[1]
        if not args:
            await message.reply("`Give Headlines For News` 🙏")
            return

        reply = message.reply_to_message
        if not (reply.photo or reply.sticker) or (reply.document and reply.document.mime_type == "application/x-tgsticker"):
            await message.reply(f"`{error_}` 🙏")
            return

        await message.delete()
        eris = await message.reply("Processing...")

        args = str(remove_emoji(args))

        if reply.sticker:
            img = await reply.download("fnewss.jpg")
        else:
            img = await reply.download()

        background = Image.open(img)

        if not os.path.exists("live_news_font.ttf"):
            await pbot.download_media(
                await pbot.get_messages("e3ris_db", ids=5904)
            )
        if not os.path.exists("live_news.png"):
            await pbot.download_media(
                await pbot.get_messages("e3ris_db", ids=5905)
            )

        news = "live_news.png"
        font = "live_news_font.ttf"

        foreground = Image.open(news)
        iin = background.resize((2800, 1500))
        iin.paste(foreground, (0, 0), mask=foreground)
        d1 = ImageDraw.Draw(iin)
        myFont = ImageFont.truetype(font, 165)
        d1.text((70, 1272), args, font=myFont, fill=(0, 0, 0))
        iin.save(img)

        await pbot.send_photo(
            message.chat.id,
            await pbot.upload_photo(img),
            reply_to_message_id=message.reply_to_message.message_id,
        )

        await eris.delete()
        if os.path.exists(img):
            os.remove(img)

@pbot.on_message(filters.command("ph"))
async def fake_comment(client, message):
    dl = "ph_comment.jpg"
    args = message.command[1]
    if not args:
        await message.reply("gib sum temxt 🌚")
        return

    args = str(remove_emoji(args))
    eris = await message.reply("🌚")
    u = pbot.get_me().username if pbot.get_me().username else pbot.get_me().first_name

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
