from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура выбора статуса привычки
status_choise_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Now"), KeyboardButton(text="Later")],
        [KeyboardButton(text="Cancel")]
    ],
    resize_keyboard=True
)


# Клавиатура подтверждения сохранения

confirm_habit_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Save")],
        [KeyboardButton(text="Edit")],
        [KeyboardButton(text="Cancel")]
    ],
    resize_keyboard=True
)