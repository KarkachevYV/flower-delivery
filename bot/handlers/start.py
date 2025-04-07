# bot/handlers/start.py
from aiogram import Router, types, Dispatcher
from aiogram.filters import Command
import aiohttp
import requests

router = Router()

API_URL = "http://127.0.0.1:8000/api/bot/users/"

async def get_or_create_user(telegram_id, username, first_name, last_name):
    """Функция проверяет, есть ли пользователь в базе, и создаёт, если нет"""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}{telegram_id}/") as response:
            if response.status == 200:
                return await response.json()  # Пользователь уже есть

        # Если пользователя нет, создаём
        user_data = {
            "telegram_id": telegram_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name
        }
        async with session.post(API_URL, json=user_data) as response:
            return await response.json()

@router.message(Command("start"))  
async def start_handler(message: types.Message):
    user = message.from_user
    first_name = user.first_name or "друг"

    # Проверяем, есть ли пользователь в БД
    api_url = f"{API_URL}{user.id}/"
    print(f"Запрашиваю API: {api_url}")

    try:
        response = requests.get(api_url)
        print("Ответ от API:", response.status_code, response.text)  # Логируем

        if response.status_code == 200:
            db_user = response.json()
            first_name = db_user.get("first_name", first_name)
        else:
            print("Пользователь не найден. Создаём нового...")

            new_user = {
                "telegram_id": user.id,
                "username": user.username or f"user_{user.id}",
                "first_name": user.first_name or "",
                "last_name": user.last_name or ""
            }

            post_response = requests.post(API_URL, json=new_user)
            print("Ответ на создание:", post_response.status_code, post_response.text)  # Лог

            if post_response.status_code == 201:
                first_name = new_user["first_name"]

    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")

    # 👉 Добавляем кнопку с запросом номера телефона
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📱 Отправить номер телефона", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        f"Добро пожаловать, {first_name}! 🎉\n\n"
        "Чтобы продолжить, пожалуйста, отправьте свой номер телефона:",
        reply_markup=keyboard
    )