from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

# from main_keyboards import main_menu
from features.habits.keyboards import habits_menu, confirm_habit_kb, status_choise_kb, did_i_know_id_habit, confirm_delete_habit_kb
from features.habits.repo import HabitsRepository
from features.habits.states import AddHabitStates, DeleteHabitStatuses


# ✅__Просмотр привычки__ show_habit
class HandlerShowHabit():
    def __init__(self, repository: HabitsRepository):
        print('✅ Habits - Handler. HandlerShowHabit зарегистрирован')
        self.router = Router()
        self.repository = repository
        self._register_handlers()

    def _register_handlers(self):
        self.router.message.register(self.show_my_habits_handler, F.text == "Show my habits")
        self.router.message.register(self.cancel_show_habits, F.text == "Cancel")

    async def show_my_habits_handler(self, message: Message):
        user_id = message.from_user.id
        habits = self.repository.show_habit(user_id)

        if not habits:
            await message.answer("You don't have any habits yet", reply_markup=habits_menu)
            return
        
        table_lines = ["<b> Your habits: </b>\n"]
        for habit in habits:
            id, name, status, time_notification, last_notification = habit
            line = f"<b>{name}</b> (at {time_notification}) - {status}"
            table_lines.append(line)

        await message.answer("\n".join(table_lines), parse_mode="HTML", reply_markup=habits_menu)
        
    async def cancel_show_habits(self, message: Message, state: FSMContext):
        await state.clear()
        await message.answer("Go to habits menu", reply_markup=habits_menu)