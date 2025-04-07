# bot\services\users.py

import aiohttp

USER_API_URL = "http://127.0.0.1:8000/api/bot/users/"

async def get_user_data(telegram_id: int) -> dict | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{USER_API_URL}{telegram_id}/") as response:
            if response.status == 200:
                return await response.json()
    return None
