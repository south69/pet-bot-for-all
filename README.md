# 🤖 Telegram Bot: Help for all
Написан на Python с использованием фреймворка `aiogram`


## Стек

- Python 3.13
- aiogram 3.17.0
- SQLite
- dotenv

## Функциональность

- 🛠 Напоминания (Reminders) - coming soon
- 🛠 Привычки (Habits) - coming soon
- ✅ Игры (Irregular Verbs)
- 🛠 Спорт (Workouts) - coming soon
- ✅ Помощь и обратная связь

## Структура проекта

```bash
.
├── functions
│   ├── games
│   │   ├── game_irregular_verbs
│   │   │   ├── game_irregular_verbs_service.py
│   │   │   ├── handler_game_irregular_verbs.py
│   │   │   └── keyboard_game_irregular_verbs.py
│   │   ├── handler_games_menu.py
│   │   └── keyboards_games.py
│   ├── habits
│   │   ├── fsm_add_habit.py
│   │   ├── handler_add_habit.py
│   │   ├── handler_habits_menu.py
│   │   ├── keyboards_add_habit.py
│   │   └── keyboards_habits.py
│   ├── help
│   │   ├── handler_help_menu.py
│   │   └── keyboards_help.py
│   ├── reminders
│   │   ├── handler_reminders_menu.py
│   │   └── keyboards_reminders.py
│   └── workouts
│       ├── settings_workout
│       │   ├── handler_settings_workout.py
│       │   └── keyboards_settings_workout.py
│       ├── start_workout
│       │   ├── handler_start_workout.py
│       │   └── keyboards_start_workout.py
│       ├── handler_workouts_menu.py
│       └── keyboards_workouts.py
├── sql_lite
│   ├── habits.db
│   ├── habits_log.csv
│   ├── habits_repository.py
│   ├── habits_task.csv
│   ├── init_db.py
│   ├── init_habits_db.py
│   ├── irregular_verbs.csv
│   ├── irregular_verbs.db
│   └── irregular_verbs_repository.py
├── .env # не публикуется
├── .gitignore # не публикуется
├── config.py
├── config_functions.py
├── docker-compose.yml
├── handler_main_menu.py
├── main.py
├── main_keyboards.py
└── requirements.txt

├── functions
│   ├── games
│   │   ├── game_irregular_verbs
│   │   │   ├── game_irregular_verbs_service.py
│   │   │   ├── handler_game_irregular_verbs.py
│   │   │   ├── irregular_verbs_repository.py
│   │   │   └── keyboard_game_irregular_verbs.py
│   │   ├── handler_games_menu.py
│   │   └── keyboards_games.py
│   ├── habits
│   │   ├── fsm_add_habit.py
│   │   ├── habits_repository.py
│   │   ├── handler_add_habit.py
│   │   ├── handler_habits_menu.py
│   │   ├── keyboards_add_habit.py
│   │   └── keyboards_habits.py
│   ├── help
│   │   ├── handler_help_menu.py
│   │   └── keyboards_help.py
│   ├── reminders
│   │   ├── handler_reminders_menu.py
│   │   └── keyboards_reminders.py
│   └── workouts
│       ├── settings_workout
│       │   ├── handler_settings_workout.py
│       │   └── keyboards_settings_workout.py
│       ├── start_workout
│       │   ├── handler_start_workout.py
│       │   └── keyboards_start_workout.py
│       ├── handler_workouts_menu.py
│       └── keyboards_workouts.py
├── initdb
│   ├── 01_create_tables.sql
│   └── 02_insert_seed_data.sql
├── Dockerfile
├── docker-compose.yml
├── README.md
├── .env # не публикуется
├── .gitignore # не публикуется
├── config.py
├── config_functions.py
├── docker-compose.yml
├── handler_main_menu.py
├── main.py
├── main_keyboards.py
└── requirements.txt
