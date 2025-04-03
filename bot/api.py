import requests
from config import DJANGO_API_URL
import aiohttp

API_BASE_URL = "http://127.0.0.1:8000/api/bot"

async def get_user(telegram_id: int):
    """Получение данных о пользователе из API."""
    url = f"{API_BASE_URL}/users/{telegram_id}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()  # Вернет данные пользователя
            return None  # Пользователь не найден

def create_order(user_id, items, total_price, address):
    url = f"{DJANGO_API_URL}create_order/"
    data = {
        "user": user_id,
        "items": items,
        "total_price": total_price,
        "address": address,
    }
    response = requests.post(url, json=data)
    return response.json()

def get_order_status(order_id):
    url = f"{DJANGO_API_URL}order_status/{order_id}/"
    response = requests.get(url)
    return response.json()

def get_user_info(user_id):
    url = f"{DJANGO_API_URL}user_info/{user_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        user = response.json()
        full_address = (
            f"{user.get('country', '')}, {user.get('region', '')}, {user.get('city', '')}, "
            f"{user.get('street', '')} {user.get('house_number', '')}, {user.get('postal_code', '')}"
        ).strip(", ")

        return {
            "username": user.get("username"),
            "email": user.get("email"),
            "phone": user.get("phone_number"),
            "role": user.get("role"),
            "address": full_address
        }
    
    return {"error": "Пользователь не найден"}


def get_analytics():
    url = f"{DJANGO_API_URL}analytics/"
    response = requests.get(url)
    return response.json()
