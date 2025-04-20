from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Main menu

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Reminders"), KeyboardButton(text="Habits")],
        [KeyboardButton(text="Games"), KeyboardButton(text='Workouts')],
        [KeyboardButton(text="Help")]
    ],
    resize_keyboard=True
)