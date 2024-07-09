from aiogram import Router, types
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(Command("pic"))
async def handle_command_pic(message: types.Message):
    url = "https://img10.reactor.cc/pics/post/Keqing-%28Genshin-Impact%29-Genshin-Impact-Genshin-Impact-Ero-poki-%28j0ch3fvj6nd%29-8473822.png"
    await message.reply_photo(
        photo=url

    )
