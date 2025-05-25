from config_functions import *

from handler_main_menu import HandlerMainMenu
from aiogram import Router


def get_all_routers() -> list[Router]:
    routers = []

    # Главное меню — FSM: MainStates.in_main_menu
    routers.append(HandlerMainMenu().router)

    # HELP — FSM: MainStates.in_help
    if ENABLE_HELP:
        try:
            from features.help.handler import HandlerHelpMenu
            routers.append(HandlerHelpMenu().router)
            print("✅ Routers registry: HandlerHelpMenu подключён")
        except Exception as e:
            print("❌ Routers registry: Ошибка в HandlerHelpMenu:", e)

    # GAMES — FSM: MainStates.in_games
    if ENABLE_GAMES:
        try:
            from features.games.handler_games_menu import HandlerGamesMenu
            from features.games.irregular_verbs.handler_game_irregular_verbs import HandlerGameIrregularVerbs
            from features.games.irregular_verbs.handler_level_game import HandlerLevelGameIrregularVerbs

            # Вложенные хендлеры — можно включить в один общий router (опционально)
            routers.append(HandlerGamesMenu().router)
            routers.append(HandlerGameIrregularVerbs().router)
            routers.append(HandlerLevelGameIrregularVerbs().router)

            print("✅ Routers registry: все обработчики Games подключены")
        except Exception as e:
            print("❌ Routers registry: Ошибка подключения Games:", e)

    # # HABITS — FSM: MainStates.in_habits
    # if ENABLE_HABITS:
    #     try:
    #         from features.habits.handler_habits_menu import HandlerHabitsMenu
    #         routers.append(HandlerHabitsMenu().router)
    #         print("✅ Routers registry: HandlerHabitsMenu подключён")
    #     except Exception as e:
    #         print("❌ Routers registry: Ошибка в HandlerHabitsMenu:", e)

    # # REMINDERS — FSM: MainStates.in_reminders
    # if ENABLE_REMINDERS:
    #     try:
    #         from features.reminders.handler_reminders_menu import HandlerRemindersMenu
    #         routers.append(HandlerRemindersMenu().router)
    #         print("✅ Routers registry: HandlerRemindersMenu подключён")
    #     except Exception as e:
    #         print("❌ Routers registry: Ошибка в HandlerRemindersMenu:", e)

    # # WORKOUTS — FSM: MainStates.in_workouts
    # if ENABLE_WORKOUTS:
    #     try:
    #         from features.workouts.handlers import HandlerWorkoutsMenu
    #         from features.workouts.settings_workout.handlers import HandlerSettingsWorkout
    #         from features.workouts.start_workout.handler import HandlerStartWorkoutMenu

    #         workouts_menu = HandlerWorkoutsMenu()
    #         workouts_settings = HandlerSettingsWorkout()
    #         workouts_start = HandlerStartWorkoutMenu()

    #         routers += [
    #             workouts_menu.router,
    #             workouts_settings.router,
    #             workouts_start.router
    #         ]

    #         print("✅ Routers registry: все обработчики Workouts подключены")
    #     except Exception as e:
    #         print("❌ Routers registry: Ошибка в Workouts:", e)

    return routers










# from config_functions import *

# from handler_main_menu import HandlerMainMenu
# from aiogram import Router


# def get_all_routers() -> list[Router]:
#     routers = []

#     # ✅ Главное меню
#     routers.append(HandlerMainMenu().router)

#     # ✅ GAMES
#     if ENABLE_GAMES:
#         try:
#             from features.games.handler_games_menu import HandlerGamesMenu
#             routers.append(HandlerGamesMenu().router)
#             print("✅ Routers registry. HandlerGamesMenu подключён")
#         except Exception as e:
#             print("❌ Routers registry. Ошибка подключения HandlerGamesMenu:", e)

#         try:
#             from features.games.irregular_verbs.handler_game_irregular_verbs import HandlerGameIrregularVerbs
#             routers.append(HandlerGameIrregularVerbs().router)
#             print("✅ Routers registry. HandlerGameIrregularVerbs подключён")
#         except Exception as e:
#             print("❌ Routers registry. Ошибка подключения HandlerGameIrregularVerbs:", e)

#         try:
#             from features.games.irregular_verbs.handler_level_game import HandlerLevelGameIrregularVerbs
#             routers.append(HandlerLevelGameIrregularVerbs().router)
#             print("✅ Routers registry. HandlerLevelGameIrregularVerbs подключён")
#         except Exception as e:
#             print("❌ Routers registry. Ошибка подключения HandlerLevelGameIrregularVerbs:", e)

    # # ✅ HABITS
    # if ENABLE_HABITS:
    #     try:
    #         from features.habits.handler_habits_menu import HandlerHabitsMenu
    #         routers.append(HandlerHabitsMenu().router)
    #         print("✅ Routers registry. HandlerHabitsMenu подключён")
    #     except Exception as e:
    #         print("❌ Routers registry. Ошибка подключения HandlerHabitsMenu:", e)


    # # ✅ HELP
    # if ENABLE_HELP:
    #     try:
    #         from features.help.handler import HandlerHelpMenu
    #         routers.append(HandlerHelpMenu().router)
    #         print("✅ Routers registry. HandlerHelpMenu подключён")
    #     except Exception as e:
    #         print("❌ Routers registry. Ошибка подключения HandlerHelpMenu:", e)

    # # ✅ REMINDERS
    # if ENABLE_REMINDERS:
    #     try:
    #         from features.reminders.handler_reminders_menu import HandlerRemindersMenu
    #         routers.append(HandlerRemindersMenu().router)
    #         print("✅ Routers registry. HandlerRemindersMenu подключён")
    #     except Exception as e:
    #         print("❌ Routers registry. Ошибка подключения HandlerRemindersMenu:", e)

    # # ✅ WORKOUTS
    # if ENABLE_WORKOUTS:
    #     try:
    #         from features.workouts.handlers import HandlerWorkoutsMenu
    #         from features.workouts.settings_workout.handlers import HandlerSettingsWorkout
    #         from features.workouts.start_workout.handler import HandlerStartWorkoutMenu

    #         # Один раз создаём и добавляем
    #         workouts_menu = HandlerWorkoutsMenu()
    #         workouts_settings = HandlerSettingsWorkout()
    #         workouts_start = HandlerStartWorkoutMenu()

    #         routers += [
    #             workouts_menu.router,
    #             workouts_settings.router,
    #             workouts_start.router
    #         ]

    #         print("✅ Все Workouts обработчики подключены")
    #     except Exception as e:
    #         print("❌ Workouts:", e)

    # return routers
