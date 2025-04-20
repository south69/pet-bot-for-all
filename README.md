# 🤖 Telegram Bot: Help for all
Написан на Python с использованием фреймворка `aiogram`


## Стек

- Python 3.13
- aiogram 3.17.0
- SQLite
- dotenv

## Функциональность

- Напоминания (Reminders) - coming soon
- Привычки (Habits) - coming soon
- Игры (Irregular Verbs)
- Спорт (Workouts) - coming soon
- Помощь и обратная связь - coming soon

## Структура проекта

```bash
.
├── functions
│   ├── games
│   │   ├── handler_games_menu.py
│   │   ├── keyboards_games.py
│   │   └── game_irregular_verbs
│   │       ├── game_irregular_verbs.py
│   │       ├── handler_game_irregular_verbs.py
│   │       └── keyboard_game_irregular_verbs.py
│   ├── habits
│   │   ├── handler_habits_menu.py
│   │   └── keyboards_habits.py
│   ├── help
│   │   ├── handler_help_menu.py
│   │   └── keyboards_help.py
│   └── reminders
│       ├── handler_reminders_menu.py
│       └── keyboards_reminders.py
├── sql_lite
│   ├── init_db.py
│   ├── irregular_verbs_repository.py
│   ├── irregular_verbs.csv
│   └── irregular_verbs.db
├── config.py              # ← загружает токен из .env
├── config_functions.py    # флаги включения модулей
├── handler_main_menu.py
├── main_keyboards.py
├── main.py
├── .env                   # (НЕ публикуется)
├── .gitignore
└── README.md