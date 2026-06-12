import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio

TOKEN = os.getenv("TOKEN") 
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message):
    await message.answer("Бот запущен на Render!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
