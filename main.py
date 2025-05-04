import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

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
        except Exception as e:
            print("Reminders: FAILED:", e)

    # HABITS
    if ENABLE_HABITS:
        try:
            from functions.habits.handler_habits_menu import HandlerHabitsMenu
            handler_habits_menu = HandlerHabitsMenu()
            dp.include_router(handler_habits_menu.router)
        except Exception as e:
            print("Habits: FAILED:", e)

    # GAMES
    if ENABLE_GAMES:
        try:
            from functions.games.handler_games_menu import HandlerGamesMenu
            handler_games_menu = HandlerGamesMenu()
            dp.include_router(handler_games_menu.router)
        except Exception as e:
            print("Games: FAILED:", e)

        # Games - Irregular Verbs
        try:
            from functions.games.game_irregular_verbs.handler_game_irregular_verbs import HandlerGameIrregularVerbs
            handler_game_irregular_verbs = HandlerGameIrregularVerbs()
            dp.include_router(handler_game_irregular_verbs.router)
        except Exception as e:
            print("Games - Irregular Verbs: FAILED:", e)

        # Games - Irregular Verbs - Level
        try:
            from functions.games.game_irregular_verbs.handler_game_irregular_verbs import HandlerLevelGameIrregularVerbs
            handler_level_game_irregular_verbs = HandlerLevelGameIrregularVerbs()
            dp.include_router(handler_level_game_irregular_verbs.router)
        except Exception as e:
            print("Games - Irregular Verbs - Level: FAILED:", e)

    # HELP
    if ENABLE_WORKOUTS:
        try:
            from functions.workouts.handler_workouts_menu import HandlerWorkoutsMenu
            handler_workouts_menu = HandlerWorkoutsMenu ()
            dp.include_router(handler_workouts_menu.router)
        except Exception as e:
            print("Workouts: FAILED:", e)

        # Workouts - settings_workouts
        try:
            from functions.workouts.settings_workout.handler_settings_workout import HandlerSettingsWorkout
            handler_settings_workout = HandlerSettingsWorkout()
            dp.include_router(handler_settings_workout.router)
        except Exception as e:
            print("Workouts - settings_workouts: FAILED:", e)

        # Workouts - start_workouts
        try:
            from functions.workouts.start_workout.handler_start_workout import HandlerStartWorkoutMenu
            handler_start_workout_menu = HandlerStartWorkoutMenu()
            dp.include_router(handler_start_workout_menu.router)
        except Exception as e:
            print("Workouts - start_workouts: FAILED:", e)


    # HELP
    if ENABLE_HELP:
        try:
            from functions.help.handler_help_menu import HandlerHelpMenu
            handler_help_menu = HandlerHelpMenu()
            dp.include_router(handler_help_menu.router)
        except Exception as e:
            print("Help: FAILED:", e)

    # Запуск бота
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

