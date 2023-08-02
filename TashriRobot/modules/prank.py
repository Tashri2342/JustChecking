import os
import emoji
import re
from PIL import Image, ImageDraw, ImageFont


def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)

@ultroid_cmd(pattern="fnews ?(.*)")
async def fake_news(e):
    if e.fwd_from:
        return
    error_ = "Reply to Sticker or Photo"
    args = e.pattern_match.group(1)
    if not args:
        await eor(e, "`Give Headlines For News` 🙏")
        return
    reply = await e.get_reply_message()
    if reply and reply.media:
        if not (reply.photo or reply.sticker) or (reply.file.ext == (".tgs")):
            await eor(e, f"`{error_}` 🙏")
            return
    else:
        await eor(e, f"`{error_}` 🙏")
        return
    eris = await eor(e, "`Processing...`")
    args = str(remove_emoji(args))
     # convert_to_image # stickers # to-do
    if reply.sticker:
        img = await reply.download_media("fnewss.jpg")
    else:
        img = await reply.download_media()
    background = Image.open(img)

    if not os.path.exists("live_news_font.ttf"):
        await ultroid_bot.download_media(
            await ultroid_bot.get_messages("e3ris_db", ids=5904)
        )
    if not os.path.exists("live_news.png"):    
        await ultroid_bot.download_media(
            await ultroid_bot.get_messages("e3ris_db", ids=5905)
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
    await ultroid_bot.send_file(
        e.chat_id,
        await ultroid_bot.upload_file(img),
        reply_to=e.reply_to_msg_id if e.is_reply else None,
    )
    await eris.delete()
    if os.path.exists(img):
        os.remove(img)



@ultroid_cmd(pattern="ph ?(.*)")
async def fake_comment(e):
    if e.fwd_from:
        return
    dl = "ph_comment.jpg"
    args = e.pattern_match.group(1)
    if not args:
        await eod(e, "`gib sum temxt` 🌚")
        return
    args = str(remove_emoji(args))
    eris = await eor(e, "🌚")
    u = bot.me.username if bot.me.username else bot.me.first_name
    if e.is_reply:
        r = await e.get_reply_message()
        u = r.sender.username if r.sender.username else r.sender.first_name
    if not os.path.exists("ph_font.TTF"):
        await ultroid_bot.download_media(
            await ultroid_bot.get_messages("e3ris_db", ids=5903)
        )
    if not os.path.exists(dl):    
        get = await ultroid_bot.get_messages("e3ris_db", ids=5909)
        dl =  await get.download_media()
    img = Image.open(dl) 
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("ph_font.TTF", 100)
    d1.text((385, 640), u, font=myFont, fill=(135, 98, 87))
    d1.text((76, 960), args, font=myFont, fill=(203, 202, 202))
    img.save("pphh.jpg")
    img = "pphh.jpg"
    await ultroid_bot.send_file(
        e.chat_id,
        await ultroid_bot.upload_file(img),
        reply_to=e.reply_to_msg_id if e.is_reply else None,
        force_document=False,
    )    
    os.remove(img)
    await eris.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})

__mod_name__ = "♨PRANKS♨️"
__help__ = """

✘ **Commands Available :**
> `{i}ph <some_text>`
> `{i}fnews <text> <reply to a picture>`

☆............𝙱𝚈 » [Tashri](https://t.me/Tashri2342)............☆
 """
