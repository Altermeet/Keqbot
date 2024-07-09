from aiogram import Router, types

router = Router(name=__name__)


@router.message()
async def echo_message(message: types.Message):



    await message.answer(
        text="Секунду...",
    )

    try:
        await message.send_copy(chat_id=message.chat.id) # метод отправляет копию текущего сообщения
    except TypeError:
        await message.reply(text="Что-то новое ^.^")
