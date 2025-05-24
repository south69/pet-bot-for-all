from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from features.workouts.keyboards import workouts_menu
from main_keyboards import main_menu

settings_workout_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Trainings")],
        [KeyboardButton(text="Exercise")],
        [KeyboardButton(text="Exit settings")]
    ],
    resize_keyboard=True
)


trainings_workout_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Show trainings")],
        [KeyboardButton(text="Edit trainings")],
        [KeyboardButton(text="Delete trainings")],
        [KeyboardButton(text="Exit trainings")]
    ],
    resize_keyboard=True
)

exercise_workout_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Show exercise")],
        [KeyboardButton(text="Edit exercise")],
        [KeyboardButton(text="Delete exercise")],
        [KeyboardButton(text="Exit exercise")]
    ],
    resize_keyboard=True
)