from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

workouts_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Start")],
        [KeyboardButton(text="Progress")],
        [KeyboardButton(text="Settings")],
        [KeyboardButton(text="Exit workouts")]
    ],
    resize_keyboard=True
)


