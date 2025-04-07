# bot/services/orders.py

import aiohttp
from aiogram import types
from aiogram.fsm.context import FSMContext
from bot.states.order_states import SomeOrderStates

API_URL = "http://127.0.0.1:8000/api/bot/orders/"
USER_API_URL = "http://127.0.0.1:8000/api/bot/users/"

ALIVE_STATUSES = ['pending', 'accepted']  # Пример статусов для "живых" заказов

async def start_orders_view(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id

    print(f"Получение заказов для пользователя с id: {telegram_id}")

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{USER_API_URL}{telegram_id}/") as response:
            if response.status == 200:
                user = await response.json()
                if "id" not in user:
                    await message.answer("Вы не привязали свой профиль. Пожалуйста, отправьте команду /profile для привязки.")
                    return
            else:
                await message.answer(f"Ошибка при проверке вашего профиля. Статус: {response.status}")
                return

        async with session.get(f"{API_URL}?user_id={telegram_id}") as response:
            if response.status == 200:
                try:
                    orders = await response.json()
                except aiohttp.ContentTypeError:
                    html_text = await response.text()
                    print(f"Получен неожиданный HTML: {html_text}")
                    await message.answer("Ошибка при обработке данных заказов, сервер вернул неожиданный ответ.")
                    return

                # Фильтрация заказов по статусу
                active_orders = [order for order in orders if order['status'] in ALIVE_STATUSES]

                if not active_orders:
                    await message.answer("У вас нет текущих заказов.")
                    return

                buttons = [types.KeyboardButton(text=f"📦 Заказ #{order['id']}") for order in active_orders]
                markup = types.ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

                await state.update_data(orders=active_orders)
                await state.set_state(SomeOrderStates.viewing)

                await message.answer("Выберите заказ для просмотра:", reply_markup=markup)
            else:
                error_text = await response.text()  # Узнать, что именно вернул сервер
                print(f"Ошибка при получении заказов. Статус: {response.status}, Ответ: {error_text}")
                await message.answer(f"Ошибка при получении заказов. Статус: {response.status}")


