from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

reminders_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Add remind")],
        [KeyboardButton(text="Change remind")],
        [KeyboardButton(text="Delete remind")],
        [KeyboardButton(text="Show my reminders")],
        [KeyboardButton(text="Back main menu")]
    ],
    resize_keyboard=True

)