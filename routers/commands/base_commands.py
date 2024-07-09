from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown

router = Router(name=__name__)


@router.message(CommandStart())


async def handle_start(message: types.Message):
    url = "https://static.tvtropes.org/pmwiki/pub/images/tartaglia_face_closeup_20.png"
    await message.answer(text=f"{markdown.hide_link(url)}Привет, {markdown.hbold(message.from_user.full_name)}!",
         parse_mode=ParseMode.HTML,# Через хайд линк вставляется картинка
                         )


@router.message(Command("help"))

# Обработка команды /help
async def handle_help(message: types.Message):

    text = "Я Кекабот\\.\nОтправь *мне* любое сообщение\\!"
    # ниже создается помощник, который всё что передано превращает в строчку и склеивает по разделителю sep
    # выделяет  жирным шрифтом, чтобы не делать вручную - не ставить звездочки
    text = markdown.text(
        "Я Кекабот\\.",  # экранирую точку. Все спец символы экранируются
        markdown.text(
            "Отправь",
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline("сообщение"),
                        "мне"),
        ),

        ),

        sep="\n",
    )
    await message.answer(
        text=text,


        parse_mode=ParseMode.MARKDOWN_V2,
    )
