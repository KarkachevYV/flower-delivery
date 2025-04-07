# bot/handlers/profile.py

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.services.orders import start_orders_view
from bot.services.users import get_user_data

import aiohttp

router = Router()

@router.message(Command("profile"))
async def profile_handler(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    user_data = await get_user_data(telegram_id)

    if user_data:
        profile_text = (
            f"👤 Профиль пользователя {user_data.get('user_username', 'неизвестен')}:\n"
            f"Имя: {user_data.get('user_first_name', '—')} {user_data.get('user_last_name', '')}\n"
            f"Телефон: {user_data.get('phone_number', 'Не указан')}\n"
            f"Email: {user_data.get('user_email', 'Не указан')}"
        )
        await message.answer(profile_text)

        # ➕ Обновим telegram_id в CustomUser (если user_id есть, но telegram_id нет)
        if user_data.get("phone_number") and user_data.get("user"):
            await update_telegram_id_in_customuser(user_data["user"], telegram_id)

            await message.answer("📦 Перехожу к списку ваших заказов...")
            await start_orders_view(message, state)
    else:
        await message.answer("❌ Профиль не найден. Пройдите /start или повторите позже.")

# 🔧 Отдельная функция для обновления telegram_id
async def update_telegram_id_in_customuser(user_id: int, telegram_id: int):
    url = f"http://127.0.0.1:8000/api/bot/users/{user_id}/"
    try:
        async with aiohttp.ClientSession() as session:
            # Получаем текущие данные
            async with session.get(url) as resp:
                if resp.status == 200:
                    user_data = await resp.json()

                    # Если telegram_id уже есть — ничего не делаем
                    if user_data.get("telegram_id"):
                        return
                    
                    # Обновляем пользователя
                    user_data["telegram_id"] = str(telegram_id)
                    async with session.put(url, json=user_data) as update_resp:
                        if update_resp.status == 200:
                            print(f"[INFO] Telegram ID добавлен пользователю #{user_id}")
                        else:
                            print(f"[ERROR] Не удалось обновить telegram_id: {await update_resp.text()}")
    except Exception as e:
        print(f"[EXCEPTION] {e}")


# @router.message(Command("edit_profile"))
# async def edit_profile_handler(message: types.Message):
#     telegram_id = message.from_user.id
#     user_data = await get_user_data(telegram_id)

#     # Если номер телефона уже есть, не просим повторно
#     if user_data and user_data.get("phone_number"):
#         await message.answer("📞 Телефон уже привязан.")
#     else:
#         await message.answer(
#             "📲 Пожалуйста, отправьте свой номер телефона через кнопку «Отправить контакт»."
#         )


# def normalize_phone(phone: str) -> str:
#     normalized = phone.replace(" ", "").replace("-", "")
#     if normalized.startswith("8"):
#         return "+7" + normalized[1:]
#     if normalized.startswith("7"):
#         return "+7" + normalized[1:]
#     if normalized.startswith("9"):
#         return "+7" + normalized
#     return normalized


# async def update_phone_number(telegram_id: int, phone_number: str):
#     url = f"{API_BASE}/link_phone/"
#     payload = {"telegram_id": telegram_id, "phone_number": phone_number}
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=payload) as resp:
#             return resp.status == 200

# @router.message(lambda m: isinstance(m.contact, Contact))
# async def update_phone_handler(message: types.Message):
#     contact = message.contact
#     telegram_id = message.from_user.id
#     phone_number = normalize_phone(contact.phone_number)

#     success = await update_phone_number(telegram_id, phone_number)

#     if success:
#         await message.answer("✅ Телефон обновлён и привязан к аккаунту!")
#     else:
#         await message.answer("❌ Не удалось привязать номер. Возможно, такой пользователь не найден на сайте.")


