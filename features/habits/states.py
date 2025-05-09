from aiogram.fsm.state import StatesGroup, State

class AddHabitStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_time = State()
    waiting_for_status = State()
    waiting_for_confirmation = State()

