from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

games_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Irregular verbs")],
        [KeyboardButton(text="Exit games")]
    ],
    resize_keyboard=True,
)