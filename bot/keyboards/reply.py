from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

request_contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Поделиться контактом", request_contact=True)]
    ],
    resize_keyboard=True
)
