from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

# from main_keyboards import main_menu
from features.habits.keyboards import habits_menu, confirm_habit_kb, status_choise_kb, did_i_know_id_habit, confirm_delete_habit_kb
from features.habits.repo import HabitsRepository
from features.habits.states import AddHabitStates, DeleteHabitStatuses



# 🟡__Изменение привычки__ change_habit
class HandlerChangeHabit():
    def __init__(self, repository: HabitsRepository):
        print('✅ Habits - Handler. HandlerChangeHabit зарегистрирован')
        self.router = Router()
        self.repository = repository
        # self._register_handlers()

        self.router.message.register(self.change_habit, F.text == "Change habit")

    async def change_habit(self, message: Message):
        await message.answer("Change habit - coming soon...", reply_markup=habits_menu)