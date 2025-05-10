from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from features.games.keyboards import games_menu
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

stats_period_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Today", callback_data="stats:today"),
            InlineKeyboardButton(text="Week", callback_data="stats:week")
        ],
        [
            InlineKeyboardButton(text="Month", callback_data="stats:month"),
            InlineKeyboardButton(text="All time", callback_data="stats:all")
        ]
    ]
)
