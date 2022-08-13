#حقوق الملف من قناة ثيند @t_hunder

#قام بتعديل الملف واضافة الميزات  @T_8_T_T
import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","المطور","السورس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/91d8df741e0758768a405.jpg",
        caption=f"""n/⍆ Welcome to the Dragon Source 🎗.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "Dragon Source", url=f"https://t.me/yy8gh"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "AHMED", url=f"https://t.me/ku_kx"
                ],
            ]
        ),
    )
