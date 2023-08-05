from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.decorators import AdminRightsCheck
from AnonXMusic.utils.database import is_music_playing, music_off


@app.on_message(
    filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Anony.pause_stream(chat_id)
    await message.reply_text(_["admin_2"].format(message.from_user.mention))
