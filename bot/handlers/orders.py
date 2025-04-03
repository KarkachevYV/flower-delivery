from aiogram import Router, types, F
from aiogram.filters import Command

from api import create_order

router = Router()

@router.message(F.text == "Заказать")
async def order_handler(message: types.Message):
    # Данные о заказе (пример)
    user_id = message.from_user.id
    items = [{"product_id": 1, "quantity": 2}]
    total_price = 1500
    address = "Москва, Тверская, 5"

    order_response = create_order(user_id, items, total_price, address)

    if "error" in order_response:
        await message.answer("Ошибка при создании заказа!")
    else:
        await message.answer(f"Ваш заказ {order_response['order']['id']} успешно оформлен!")
