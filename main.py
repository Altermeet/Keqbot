import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from routers import router as main_router
import config
dp = Dispatcher()
dp.include_router(main_router)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=config.TOKEN_BOT)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())