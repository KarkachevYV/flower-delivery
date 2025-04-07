# bot/utils/navigation.py

from aiogram import types
from bot.handlers.orders import orders_handler

async def go_to_orders(message: types.Message):
    await message.answer("📦 Загружаю ваши заказы...")
    await orders_handler(message)
