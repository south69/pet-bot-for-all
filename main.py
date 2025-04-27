import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from sql_lite.init_db import create_irregular_verbs_table
from sql_lite.init_habits_db import create_habits_tables

# НУЖНО ИСПРАВИТЬ ОБРАБОТЧИКИ В БЛОКЕ WORKOUTS, ПЕРЕСКАКИВАЕТ ИНОГДА НА GAME МЕНЮ 

from config import api_token_tg

from config_functions import (
    ENABLE_REMINDERS,
    ENABLE_HABITS,
    ENABLE_GAMES,
    ENABLE_WORKOUTS,
    ENABLE_HELP
)

from handler_main_menu import HandlerMainMenu
from main_keyboards import main_menu
# from functions.help.handler_help_menu import HandlerHelpMenu

async def main():
    logging.basicConfig(level=logging.INFO)
    create_irregular_verbs_table()
    create_habits_tables()

    bot = Bot(
        token=api_token_tg, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher(storage=MemoryStorage())

    handler_main_menu = HandlerMainMenu()
    dp.include_router(handler_main_menu.router)

    # REMINDERS
    if ENABLE_REMINDERS:
        try:
            from functions.reminders.handler_reminders_menu import HandlerRemindersMenu
            handler_reminders_menu = HandlerRemindersMenu()
            dp.include_router(handler_reminders_menu.router)
        except ImportError:
            print('Module not in work')

    # HABITS
    if ENABLE_HABITS:
        try:
            from functions.habits.handler_habits_menu import HandlerHabitsMenu
            handler_habits_menu = HandlerHabitsMenu()
            dp.include_router(handler_habits_menu.router)
        except ImportError:
            print('Module not in work')

    # GAMES
    if ENABLE_GAMES:
        try:
            from functions.games.handler_games_menu import HandlerGamesMenu
            handler_games_menu = HandlerGamesMenu()
            dp.include_router(handler_games_menu.router)
        except ImportError:
            print('Module not in work')

        # Games - Irregular Verbs
        try:
            from functions.games.game_irregular_verbs.handler_game_irregular_verbs import HandlerGameIrregularVerbs
            handler_game_irregular_verbs = HandlerGameIrregularVerbs()
            dp.include_router(handler_game_irregular_verbs.router)
        except ImportError:
            print('Module not in work')

        # Games - Irregular Verbs - Level
        try:
            from functions.games.game_irregular_verbs.handler_game_irregular_verbs import HandlerLevelGameIrregularVerbs
            handler_level_game_irregular_verbs = HandlerLevelGameIrregularVerbs()
            dp.include_router(handler_level_game_irregular_verbs.router)
        except ImportError:
            print("Module not in work")

    # HELP
    if ENABLE_WORKOUTS:
        try:
            from functions.workouts.handler_workouts_menu import HandlerWorkoutsMenu
            handler_workouts_menu = HandlerWorkoutsMenu ()
            dp.include_router(handler_workouts_menu.router)
        except ImportError:
            print("Module not in Work")

        # Workouts - settings_workouts
        try:
            from functions.workouts.settings_workout.handler_settings_workout import HandlerSettingsWorkout
            handler_settings_workout = HandlerSettingsWorkout()
            dp.include_router(handler_settings_workout.router)
        except ImportError:
            print("Module not in work")

        # Workouts - start_workouts
        try:
            from functions.workouts.start_workout.handler_start_workout import HandlerStartWorkoutMenu
            handler_start_workout_menu = HandlerStartWorkoutMenu()
            dp.include_router(handler_start_workout_menu.router)
        except ImportError:
            print("Module not in work")


    # HELP
    if ENABLE_HELP:
        try:
            from functions.help.handler_help_menu import HandlerHelpMenu
            handler_help_menu = HandlerHelpMenu()
            dp.include_router(handler_help_menu.router)
        except ImportError:
            print('Module not in Work')

    # Запуск бота
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

