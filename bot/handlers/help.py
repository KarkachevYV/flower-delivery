from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=['help']))
async def help_cmd(message: Message):
    """Вывод списка команд"""
    help_text = (
        "🛠 Доступные команды:\n\n"
        "📌 /start — Запустить бота и добавить заметку, напоминание, задачу или расписание.\n"
        "📌 /profile — Ваш профиль в телеграмм.\n"
        "📌 /orders — Ваши заказы.\n"
        "📌 /reviews — Оставить отзыв (указать рейтинг).\n"
        "📌 /link_profile — Ваш профиль на сайте.\n"
        "📌 /notifications — Ваши уведомления.\n"   
    )
    await message.answer(help_text)