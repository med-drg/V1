#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
force_btn = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="اشترك هنا", url="https://t.me/yy8gg"
            ),                        
        ],        
    ]
)

async def check_is_joined(message):    
    try:
        userid = message.from_user.id
        status = await app.get_chat_member("yy8gg", userid)
        return True
    except Exception:
        await message.reply_text("عذرا ؏ُـمريـہ أنت غير مشترك في @YY8GG ** \n**انضم لتستطيع تشغيل الاغاني**",reply_markup=force_btn,parse_mode="markdown",disable_web_page_preview=False)
        return False

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Yukki.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
