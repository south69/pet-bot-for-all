from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from functions.games.keyboards_games import games_menu
from functions.workouts.keyboards_workouts import workouts_menu
from main_keyboards import main_menu

start_workout_choose_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Select training")],
        [KeyboardButton(text="Choose training")],
        [KeyboardButton(text="Go back to workouts menu")]
    ],
    resize_keyboard=True
)


