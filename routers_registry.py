from config_functions import *
from handler_main_menu import HandlerMainMenu

def get_all_routers():
    from aiogram import Router

    main_menu = HandlerMainMenu().router
    routers = [main_menu]

    if ENABLE_GAMES:
        try:
            from features.games.handlers import HandlerGamesMenu
            from features.games.irregular_verbs.handlers import HandlerGameIrregularVerbs, HandlerLevelGameIrregularVerbs
            routers += [
                HandlerGamesMenu().router,
                HandlerGameIrregularVerbs().router,
                HandlerLevelGameIrregularVerbs().router,
            ]
        except Exception as e:
            print("Games: FAILED:", e)
    
    if ENABLE_HABITS:
        try:
            from features.habits.handlers import HandlerHabitsMenu
            routers.append(HandlerHabitsMenu().router)
        except Exception as e:
            print("Habits: FAILED:", e)  

    if ENABLE_HELP:
        try:
            from features.help.handler import HandlerHelpMenu
            routers.append(HandlerHelpMenu().router)
        except Exception as e:
            print("Help: FAILED:", e)          

    if ENABLE_REMINDERS:
        try:
            from features.reminders.handler_reminders_menu import HandlerRemindersMenu
            routers.append(HandlerRemindersMenu().router)
        except Exception as e:
            print("Reminders: FAILED:", e)

    if ENABLE_WORKOUTS:
        try:
            from features.workouts.handlers import HandlerWorkoutsMenu
            from features.workouts.settings_workout.handlers import HandlerSettingsWorkout
            from features.workouts.start_workout.handler import HandlerStartWorkoutMenu
            routers += [
                HandlerWorkoutsMenu().router,
                HandlerSettingsWorkout().router,
                HandlerStartWorkoutMenu().router,
            ]
        except Exception as e:
            print("Workouts: FAILED:", e)

    return routers