import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types
from aiogram.filters import Command
from aiogram.types import BotCommand

from handlers import handler, exercises

from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv
import os

PROXY_URL = "http://proxy.server:3128"
session = AiohttpSession(proxy=PROXY_URL)

dp = Dispatcher(storage=MemoryStorage())

commands = [
    "/cancel - завершить выполнение задания",
    "/help - вся информация",
    "/grammar - задания на грамматику",
    "/vocabulary - задания на лексику",
    "/word_formation - задания на словообразование",
]


@dp.message(Command("help"))
async def hlp(message: types.Message):
    msg = '\n'.join(commands)
    await message.answer(
        text=msg,
    )

@dp.message(Command("start"))
async def start(message: types.Message):
    msg = '\n'.join(commands)
    await message.answer(
        text=msg,
    )


async def main():
    load_dotenv()
    token = os.environ.get("token")

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=token)
    #bot = Bot(token=token, session=session)

    commands = [
        BotCommand(command="help", description="вся информация"),
        BotCommand(command="grammar", description="задания на грамматику"),
        BotCommand(command="vocabulary", description="задания на лексику"),
        BotCommand(command="word_formation", description="задания на словообразование"),
        BotCommand(command="cancel", description="завершить выполнение задания"),
    ]
    await bot.set_my_commands(commands)

    dp.include_router(exercises.router)
    dp.include_router(handler.router)

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":


    asyncio.run(main())