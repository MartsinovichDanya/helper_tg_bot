import asyncio
import logging
from os import getenv

from handlers.echo import echo_router
from handlers.start import start_router

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        start_router,
        echo_router,
    )

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())