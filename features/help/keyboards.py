from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

help_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="About Bot")],
        [KeyboardButton(text="Suggest update")],
        [KeyboardButton(text="Bug report")],
        [KeyboardButton(text="Ask developer")],
        [KeyboardButton(text="Exit help")]
    ],
    resize_keyboard=True

)