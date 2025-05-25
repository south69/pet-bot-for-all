from aiogram.fsm.state import StatesGroup, State

class MainStates(StatesGroup):
    in_main_menu = State()
    in_games = State()
    in_habits = State()
    in_help = State()
    in_reminders = State()
    in_workouts = State()