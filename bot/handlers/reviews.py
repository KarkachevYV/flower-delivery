# # bot\handlers\reviews.py

# from aiogram import Router
# from aiogram.types import Message
# from bot.models import get_or_create_bot_user
# from orders.models import Review
# from asgiref.sync import sync_to_async

# router = Router()


# @sync_to_async
# def get_user_reviews(customuser):
#     return list(Review.objects.filter(user__customuser=customuser).select_related('order'))


# @router.message(lambda msg: msg.text.lower() == "/reviews")
# async def get_reviews(message: Message):
#     bot_user = await get_or_create_bot_user(message.from_user)

#     if not bot_user.customuser:
#         await message.answer("❌ Сначала привяжите свой профиль командой /start.")
#         return

#     reviews = await get_user_reviews(bot_user.customuser)

#     if not reviews:
#         await message.answer("😔 Вы ещё не оставляли отзывов.")
#         return

#     response = "📝 Ваши отзывы:\n\n"
#     for review in reviews:
#         response += f"Заказ #{review.order.id} — Оценка: {review.rating}/5\n\"{review.text}\"\n\n"

#     await message.answer(response)
