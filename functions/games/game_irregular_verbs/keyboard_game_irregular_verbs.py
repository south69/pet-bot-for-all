from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from functions.games.keyboards_games import games_menu
from main_keyboards import main_menu

games_irregular_verbs_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Play")],
        [KeyboardButton(text="Statistics")],
        [KeyboardButton(text="Rules")],
        [KeyboardButton(text="Back main menu")]
    ],
    resize_keyboard=True
)

games_irregular_verbs_choose_level = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Easy")],
        [KeyboardButton(text="Medium")],
        [KeyboardButton(text="Hard")],
        [KeyboardButton(text="Go back")]
    ],
    resize_keyboard=True
)


