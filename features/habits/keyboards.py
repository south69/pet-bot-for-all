from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main_keyboards import main_menu

habits_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Add habit")],
        [KeyboardButton(text="Change habit")],
        [KeyboardButton(text="Delete habit")],
        [KeyboardButton(text="Show my habits")],
        [KeyboardButton(text="Exit habits")]
    ],
    resize_keyboard=True

)

# __Добавление привычки__
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

# __Удаление привычки__

# Клавиатура для выбора "Я знаю id привычки, которую хочу удалить?"
did_i_know_id_habit = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="I know")],
        [KeyboardButton(text="Don't know")]
    ]
)

# Клавиатура подтверждения удаления
confirm_delete_habit_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Delete')],
        [KeyboardButton(text='Cancel')]
    ],
    resize_keyboard=True
)