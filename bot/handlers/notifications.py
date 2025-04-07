# from aiogram import types
# from aiogram.utils.keyboard import InlineKeyboardBuilder

# async def notify_order_delivered(bot, telegram_id, order_id):
#     builder = InlineKeyboardBuilder()
#     builder.button(text="⭐️ Оценить", callback_data=f"rate_{order_id}")
#     builder.button(text="💬 Оставить отзыв", callback_data=f"review_{order_id}")
#     builder.adjust(1)

#     await bot.send_message(
#         chat_id=telegram_id,
#         text=f"Ваш заказ №{order_id} был доставлен! 🚚\nОцените, пожалуйста, наш сервис:",
#         reply_markup=builder.as_markup()
#     )
