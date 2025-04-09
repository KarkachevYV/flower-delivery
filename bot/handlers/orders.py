# bot/handlers/orders.py

from aiogram import Router,  types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
# from bot.states.order_states import SomeOrderStates
from bot.services.orders import start_orders_view
import aiohttp
from ..config import API_URL  # Относительный импорт

router = Router()

@router.message(Command("orders"))
async def orders_command_handler(message: Message, state: FSMContext):
    await start_orders_view(message, state)


router = Router()

@router.callback_query(F.data.startswith("order_detail:"))
async def show_order_detail(callback: CallbackQuery):
    order_id = callback.data.split(":")[1]
    url = f"{API_URL}/api/bot/orders/{order_id}/"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={"telegram_id": callback.from_user.id}) as response:
            if response.status == 200:
                order_data = await response.json()

                text = (
                    f"📦 <b>Заказ #{order_data['id']}</b>\n"
                    f"📅 Дата: {order_data['created_at'][:10]}\n"
                    f"📝 Статус: {order_data['status']}\n"
                    f"🏠 Адрес: {order_data['address']}\n"
                    f"📞 Телефон: {order_data['phone']}\n\n"
                    f"<b>Товары:</b>\n"
                )
                for item in order_data['items']:
                    text += f"• {item['flower']} — {item['quantity']} шт. по {item['price']}₽\n"

                text += f"\n💰 <b>Итого:</b> {order_data['total_price']}₽"
                await callback.message.edit_text(text, parse_mode='HTML')
            else:
                await callback.message.edit_text("Не удалось получить детали заказа.")


@router.message(F.text.startswith("📦 Заказ #"))
async def handle_order_text(message: Message):
    try:
        order_id = int(message.text.replace("📦 Заказ #", "").strip())
    except ValueError:
        await message.answer("Не удалось определить номер заказа.")
        return

    await message.answer(f"Пожалуйста, подождите, загружаю заказ #{order_id}...")

    url = f"{API_URL}/api/bot/orders/{order_id}/"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={"telegram_id": message.from_user.id}) as response:
            if response.status == 200:
                order_data = await response.json()

                text = (
                    f"📦 <b>Заказ #{order_data['id']}</b>\n"
                    f"📅 Дата: {order_data['created_at'][:10]}\n"
                    f"📝 Статус: {order_data['status']}\n"
                    f"🏠 Адрес: {order_data['address']}\n"
                    f"📞 Телефон: {order_data['phone']}\n\n"
                    f"<b>Товары:</b>\n"
                )
                for item in order_data['items']:
                    text += f"• {item['flower']} — {item['quantity']} шт. по {item['price']}₽\n"
                text += f"\n💰 <b>Итого:</b> {order_data['total_price']}₽"
                
                await message.answer(text, parse_mode='HTML')
            else:
                await message.answer("Не удалось получить детали заказа.")



# API_BASE = "http://127.0.0.1:8000/api/bot"

# async def get_user_orders(telegram_id: int):
#     url = f"{API_BASE}/orders/?user_id={telegram_id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 200:
#                 return await resp.json()
#     return []

# async def get_order_status(order_id: int):
#     url = f"{API_BASE}/orders/{order_id}/"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 200:
#                 return await resp.json()
#     return None


# async def update_order_status(order_id: int, new_status: str):
#     url = f"{API_BASE}/orders/{order_id}/"
#     payload = {"status": new_status}
#     async with aiohttp.ClientSession() as session:
#         async with session.put(url, json=payload) as resp:
#             return resp.status == 200


# @router.message(Command("order_status"))
# async def order_status_handler(message: types.Message):
#     parts = message.text.split()
#     if len(parts) < 2 or not parts[1].isdigit():
#         return await message.answer("⚠️ Укажите ID заказа, например: /order_status 42")

#     order_id = int(parts[1])
#     order = await get_order_status(order_id)

#     if order:
#         await message.answer(f"📦 Заказ #{order['id']} — статус: {order['status']}")
#     else:
#         await message.answer("❌ Заказ не найден.")


# @router.message(Command("update_order_status"))
# async def update_order_status_handler(message: types.Message):
#     parts = message.text.split()
#     if len(parts) < 3 or not parts[1].isdigit():
#         return await message.answer("⚠️ Используйте формат: /update_order_status 42 delivered")

#     order_id = int(parts[1])
#     new_status = parts[2]

#     success = await update_order_status(order_id, new_status)

#     if success:
#         await message.answer(f"✅ Статус заказа #{order_id} обновлён на {new_status}.")
#     else:
#         await message.answer("❌ Не удалось обновить статус.")