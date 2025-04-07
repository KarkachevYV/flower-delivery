# from aiogram import Router, types, F
# from aiogram.types import Message, CallbackQuery
# from keyboards.inline import admin_analytics_buttons
# from services.analytics import get_analytics_data
# from utils.access import is_admin

# router = Router()

# @router.message(F.text == "/admin_analytics")
# async def admin_panel(message: Message):
#     if not is_admin(message.from_user.id):
#         await message.answer("⛔️ Доступ запрещён")
#         return
#     await message.answer("Выберите период:", reply_markup=admin_analytics_buttons())

# @router.callback_query(F.data.startswith("analytics_"))
# async def show_analytics(callback: CallbackQuery):
#     period = callback.data.split("_")[1]
#     stats = get_analytics_data(period)
#     await callback.message.answer(stats)
