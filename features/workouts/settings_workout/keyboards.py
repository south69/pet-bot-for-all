from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from features.workouts.keyboards import workouts_menu
from main_keyboards import main_menu

settings_workout_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Trainings")],
        [KeyboardButton(text="Exercise")],
        [KeyboardButton(text="Go back to workouts menu")]
    ],
    resize_keyboard=True
)


trainings_workout_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Show trainings")],
        [KeyboardButton(text="Edit stainings")],
        [KeyboardButton(text="Delete stainings")],
        [KeyboardButton(text="Go back")]
    ],
    resize_keyboard=True
)

exercise_workout_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Show exercise")],
        [KeyboardButton(text="Edit exercise")],
        [KeyboardButton(text="Delete exercise")],
        [KeyboardButton(text="Go back")]
    ],
    resize_keyboard=True
)