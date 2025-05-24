from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from features.workouts.keyboards import workouts_menu

from main_keyboards import main_menu

start_workout_choose_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Select training")],
        [KeyboardButton(text="Choose training")],
        [KeyboardButton(text="Exit training")]
    ],
    resize_keyboard=True
)


