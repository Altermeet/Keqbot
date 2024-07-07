import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
# объясняю диспетчеру как передать команду. Командстарт обрабатывает все боты
from aiogram.filters import CommandStart, Command
# импортирую помощник маркдаун (всё что касается разметки) из библиотеки айограм
from aiogram.utils import markdown
from aiogram.enums import ParseMode



import config


dp = Dispatcher()


# декорирую и указываю какие сообщения готов принимать. указываю Командстарт.
# ожидается, что будет Старт. Указываю экземпляр этого класса.
@dp.message(CommandStart())
# функция хэндл старт обрабатывает сообщение Start
# фулл нейм проверяет есть ли ластнейм то фёрстнейм и ластнейм ставятся через пробел
# если нет ластнейм, то возвращается только фёрстнейм. Фёрстнейм в ТГ есть у всех

async def handle_start(message: types.Message):
    url = "https://static.tvtropes.org/pmwiki/pub/images/tartaglia_face_closeup_20.png"
    await message.answer(text=f"{markdown.hide_link(url)}Привет, {markdown.hbold(message.from_user.full_name)}!",
         parse_mode=ParseMode.HTML,# Через хайд линк вставляется картинка
                         )


#выше указываю разметку через HTML
#hbold - HTML bold


# слэш (/) не указывать. т.к обрабатываю команду help, а не команду команда хелп(/help)
# по умолчанию слеш (/) значение, которое будет искаться вначале сообщения.
# поэтому Командхэлп достаточно чтобы обработать команду help

@dp.message(Command("help"))

# Обработка команды /help
async def handle_help(message: types.Message):
    # указываю в тексте что (мне) будет жирным шрифтом

    # text = "Я Кекабот.\nОтправь мне любое сообщение!"
    # entity_bold = types.MessageEntity(
    #    type="bold",  #Жирный шрифт. *слово* выделение слова, которое будет жирным
    #    offset=len("Я Кекабот.\nОтправь "),
    #    length=3,               #длина 3 символа (мне)
    # )
    # entities = [entity_bold]
    text = "Я Кекабот\\.\nОтправь *мне* любое сообщение\\!"
    # ниже создается помощник, который всё что передано превращает в строчку и склеивает по разделителю sep
    # выделяет  жирным шрифтом, чтобы не делать вручную - не ставить звездочки
    text = markdown.text(
        "Я Кекабот\\.",  # экранирую точку. Все спец символы экранируются
        markdown.text(
            "Отправь",
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline("сообщение"), # underline подчеркивает слова в текущем случае сообщение
                        "мне"),  #делаю жирным только это сообщение "сообщение\\!"),
        ),

        ),
        # к строчке ниже, всё что туда накидал будет разделено новой строкой
        sep="\n",
    )
    await message.answer(
        text=text,


        parse_mode=ParseMode.MARKDOWN_V2,
    )



# обработчик. Ассинхронная функция. Бот отвечает тем, что ему написали.
@dp.message()
async def echo_message(message: types.Message):
    # bot.send_message Обращение к боту, которое работает по токену и с него метод сэндмесседж, который отправляет сообщения



    # await bot.send_message(
    #    chat_id=message.chat.id,
    #   text="Wait a second...",
    # )

    await message.answer(
        text="Секунду...",
    )
    # if message.text:
    #    await message.answer(
    #        text=message.text,
    #        entities=message.entities,
    #    )
    try:
        await message.send_copy(chat_id=message.chat.id) # метод отправляет копию текущего сообщения
    except TypeError:
        await message.reply(text="Что-то новое ^.^")



# функция для запуска бота
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=config.TOKEN_BOT)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
