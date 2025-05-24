from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

# from main_keyboards import main_menu
from features.habits.keyboards import habits_menu, confirm_habit_kb, status_choise_kb, did_i_know_id_habit, confirm_delete_habit_kb
from features.habits.repo import HabitsRepository
from features.habits.states import AddHabitStates, DeleteHabitStatuses


# 🟡__Удаление привычки__ delete_habit
class HandlerDeleteHabit():
    def __init__(self, repository: HabitsRepository):
        print('✅ Habits - Handler. HandlerDeleteHabit зарегистрирован')
        self.router = Router()
        self.repository = repository
        
        
        
        self.router.message.register(self.delete_habit, F.text == "Delete habit")

    async def delete_habit(self, message: Message):
        await message.answer("Delete habit - coming soon...", reply_markup=habits_menu)