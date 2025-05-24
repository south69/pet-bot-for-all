from config_functions import *

from handler_main_menu import HandlerMainMenu
from aiogram import Router


def get_all_routers() -> list[Router]:
    routers = []

    # ✅ Главное меню
    routers.append(HandlerMainMenu().router)

    # ✅ GAMES
    if ENABLE_GAMES:
        try:
            from features.games.handler_games_menu import HandlerGamesMenu
            routers.append(HandlerGamesMenu().router)
            print("✅ Routers registry. HandlerGamesMenu подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerGamesMenu:", e)

        try:
            from features.games.irregular_verbs.handler_game_irregular_verbs import HandlerGameIrregularVerbs
            routers.append(HandlerGameIrregularVerbs().router)
            print("✅ Routers registry. HandlerGameIrregularVerbs подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerGameIrregularVerbs:", e)

        try:
            from features.games.irregular_verbs.handler_level_game import HandlerLevelGameIrregularVerbs
            routers.append(HandlerLevelGameIrregularVerbs().router)
            print("✅ Routers registry. HandlerLevelGameIrregularVerbs подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerLevelGameIrregularVerbs:", e)

    # ✅ HABITS
    if ENABLE_HABITS:
        try:
            from features.habits.handler_habits_menu import HandlerHabitsMenu
            routers.append(HandlerHabitsMenu().router)
            print("✅ Routers registry. HandlerHabitsMenu подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerHabitsMenu:", e)


    # ✅ HELP
    if ENABLE_HELP:
        try:
            from features.help.handler import HandlerHelpMenu
            routers.append(HandlerHelpMenu().router)
            print("✅ Routers registry. HandlerHelpMenu подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerHelpMenu:", e)

    # ✅ REMINDERS
    if ENABLE_REMINDERS:
        try:
            from features.reminders.handler_reminders_menu import HandlerRemindersMenu
            routers.append(HandlerRemindersMenu().router)
            print("✅ Routers registry. HandlerRemindersMenu подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerRemindersMenu:", e)

    # ✅ WORKOUTS
    if ENABLE_WORKOUTS:
        try:
            from features.workouts.handlers import HandlerWorkoutsMenu
            routers.append(HandlerWorkoutsMenu().router)
            print("✅ Routers registry. HandlerWorkoutsMenu подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerWorkoutsMenu:", e)

        try:
            from features.workouts.settings_workout.handlers import HandlerSettingsWorkout
            routers.append(HandlerSettingsWorkout().router)
            print("✅ Routers registry. HandlerSettingsWorkout подключён")
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerSettingsWorkout:", e)

        try:
            from features.workouts.start_workout.handler import HandlerStartWorkoutMenu
            routers += [
                HandlerWorkoutsMenu().router,
                HandlerSettingsWorkout().router,
                HandlerStartWorkoutMenu().router,
            ]
        except Exception as e:
            print("❌ Routers registry. Ошибка подключения HandlerStartWorkoutMenu:", e)

    return routers
