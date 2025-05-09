from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

games_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Irregular verbs (English)")],
        [KeyboardButton(text="Back main menu")]
    ],
    resize_keyboard=True

)