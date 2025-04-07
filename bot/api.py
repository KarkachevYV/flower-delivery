# bot/api.py

import aiohttp
import logging

API_URL = "http://127.0.0.1:8000/api/bot/users/"
TIMEOUT = aiohttp.ClientTimeout(total=5)  # Максимум 5 секунд на запрос

# Настройка логирования
logger = logging.getLogger(__name__)


async def get_user_data(telegram_id: int) -> dict | None:
    url = f"{API_URL}{telegram_id}/"
    try:
        async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                logger.warning(f"⚠️ Не удалось получить данные пользователя {telegram_id}: {response.status}")
    except aiohttp.ClientError as e:
        logger.error(f"🚫 Ошибка запроса при получении данных профиля: {e}")
    return None


async def update_phone_number(telegram_id: int, phone_number: str) -> bool:
    url = f"{API_URL}{telegram_id}/"
    data = {
        "telegram_id": telegram_id,
        "phone_number": phone_number
    }

    try:
        async with aiohttp.ClientSession(timeout=TIMEOUT) as session:
            async with session.put(url, json=data) as response:
                if response.status == 200:
                    return True
                logger.warning(f"⚠️ Не удалось обновить телефон {telegram_id}: {response.status}")
    except aiohttp.ClientError as e:
        logger.error(f"🚫 Ошибка запроса при обновлении телефона: {e}")
    return False
