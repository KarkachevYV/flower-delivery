# bot/handlers/link_profile.py
import logging
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, Contact
import aiohttp

router = Router()
logger = logging.getLogger(__name__)

API_URL = "http://127.0.0.1:8000/api/bot/link_phone/"


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Добро пожаловать, Каркач! 🎉\n\nЧтобы продолжить, пожалуйста, отправьте свой номер телефона:")


@router.message(lambda m: isinstance(m.contact, Contact))
async def link_profile(message: Message):
    contact = message.contact
    telegram_id = message.from_user.id
    phone_number = contact.phone_number

    logger.debug(f"Получен контакт от пользователя {telegram_id}: {phone_number}")

    # Нормализация телефона
    normalized_phone = phone_number.replace(" ", "").replace("-", "")
    if normalized_phone.startswith("8"):
        normalized_phone = "+7" + normalized_phone[1:]
    elif normalized_phone.startswith("7"):
        normalized_phone = "+7" + normalized_phone[1:]
    elif normalized_phone.startswith("9"):
        normalized_phone = "+7" + normalized_phone

    logger.debug(f"Нормализованный номер: {normalized_phone}")

    data = {
        "telegram_id": telegram_id,
        "phone_number": normalized_phone
    }

    logger.debug(f"Отправляем данные на сервер: {data}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, json=data) as response:
                response_text = await response.text()
                logger.debug(f"Ответ от API: Статус {response.status}, тело: {response_text[:300]}...")

                if response.status == 200:
                    await message.answer("✅ Профиль успешно привязан!")
                else:
                    await message.answer("❌ Не удалось привязать профиль. Проверьте номер телефона.")

    except Exception as e:
        logger.error(f"Ошибка при запросе к API: {e}")
        await message.answer("❌ Произошла ошибка при подключении к серверу. Попробуйте позже.")
