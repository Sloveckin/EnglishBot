import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types
from aiogram.filters import Command




from handlers import handler, exercises

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7619048729:AAHBgOTh5AMxvF1oAjl2k8eu-Ypt2ELew2k")
dp = Dispatcher(storage=MemoryStorage())




commands = [
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

    dp.include_router(exercises.router)
    dp.include_router(handler.router)

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())