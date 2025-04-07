# bot/main.py        
import asyncio
from aiogram import Bot, Dispatcher
from bot.handlers import help, start, link_profile, profile, orders# , reviews
from bot.config import TOKEN
import sys
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()  # Убираем dp из start.py, создаём его только тут
    
    dp.include_router(help.router)
    dp.include_router(start.router)
    dp.include_router(link_profile.router)
    dp.include_router(orders.router)
    # dp.include_router(reviews.router)
    dp.include_router(profile.router)

    print("🚀 Бот запущен! Нажмите Ctrl + C для выхода.")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("✅ Сессия бота закрыта.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n❌ Бот выключен через Ctrl + C.")