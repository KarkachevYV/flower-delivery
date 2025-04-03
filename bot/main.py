# bot/main.py        
import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from handlers import start, orders

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()  # Убираем dp из start.py, создаём его только тут

    dp.include_router(start.router)
    dp.include_router(orders.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
