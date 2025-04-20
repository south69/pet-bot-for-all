from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

habits_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Add habit")],
        [KeyboardButton(text="Change habit")],
        [KeyboardButton(text="Delete habit")],
        [KeyboardButton(text="Show my habits")],
        [KeyboardButton(text="Back main menu")]
    ],
    resize_keyboard=True

)