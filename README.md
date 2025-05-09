# 🤖 Telegram Bot: Help for all
Version 1.1


## Стек

- Python 3.11
- aiogram 3.17.0
- Postgres
- Docker
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
├── config
│   ├── config.py
│   └── config_functions.py
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
├── features
│   ├── games
│   │   ├── irregular_verbs
│   │   │   ├── handlers.py
│   │   │   ├── keyboards.py
│   │   │   ├── repo.py
│   │   │   └── service.py
│   │   ├── handlers.py
│   │   └── keyboards.py
│   ├── habits
│   │   ├── handlers.py
│   │   ├── keyboards.py
│   │   ├── repo.py
│   │   └── states.py
│   ├── help
│   │   ├── handler.py
│   │   └── keyboards.py
│   ├── reminders
│   │   ├── handler_reminders_menu.py
│   │   └── keyboards.py
│   └── workouts
│       ├── settings_workout
│       │   ├── handlers.py
│       │   └── keyboards.py
│       ├── start_workout
│       │   ├── handler.py
│       │   └── keyboards.py
│       ├── handlers.py
│       └── keyboards.py
├── initdb
│   ├── 01_create_tables.sql
│   └── 02_insert_seed_data.sql
├── .env # не публикуется
├── .gitignore # не публикуется
├── README.md
├── Dockerfile
├── docker-compose.yml
├── handler_main_menu.py
├── main.py
├── main_keyboards.py
└── requirements.txt
