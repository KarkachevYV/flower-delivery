from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def order_buttons(order_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝 Оставить отзыв", callback_data=f"review_{order_id}")],
        [InlineKeyboardButton(text="⭐️ Оценить заказ", callback_data=f"rate_{order_id}")]
    ])

def admin_analytics_buttons():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Аналитика за сегодня", callback_data="analytics_today")],
        [InlineKeyboardButton(text="📈 За неделю", callback_data="analytics_week")]
    ])


def generate_orders_keyboard(order_list):
    keyboard = InlineKeyboardMarkup()
    for order in order_list:
        keyboard.add(
            InlineKeyboardButton(
                text=f"📦 Заказ #{order['id']}",
                callback_data=f"order_detail:{order['id']}"
            )
        )
    return keyboard


