from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

from functions.habits.fsm_add_habit import AddHabitStates
from functions.habits.keyboards_add_habit import confirm_habit_kb, status_choise_kb
from functions.habits.keyboards_habits import habits_menu
from functions.habits.habits_repository import HabitsRepository


class HandlerAddHabit:
    def __init__(self, repository: HabitsRepository):
        self.router = Router()
        self.repository = repository
        self._register_handlers()

    def _register_handlers(self):

        self.router.message.register(self.cancel_add_habit, F.text == "Cancel")

        self.router.message.register(self.start_add_habit, F.text == "Add habit")
        self.router.message.register(self.habit_get_name, AddHabitStates.waiting_for_name)
        self.router.message.register(self.habit_get_time, AddHabitStates.waiting_for_time)
        self.router.message.register(self.habit_get_status, AddHabitStates.waiting_for_status)
        self.router.message.register(self.habit_confirmation, AddHabitStates.waiting_for_confirmation)

    async def cancel_add_habit(self, message: Message, state: FSMContext):
        await state.clear()
        await message.answer("Habit creation cancelled", reply_markup=habits_menu)
    
    async def start_add_habit(self, message: Message, state: FSMContext):
        await message.answer("Write habit name", reply_markup=ReplyKeyboardRemove())
        await state.set_state(AddHabitStates.waiting_for_name)

    async def habit_get_name(self, message: Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer("Choose a time, like 08:00")
        await state.set_state(AddHabitStates.waiting_for_time)

    async def habit_get_time(self, message: Message, state: FSMContext):
        await state.update_data(time_notification=message.text)
        await message.answer("Activate now or later?", reply_markup=status_choise_kb)
        await state.set_state(AddHabitStates.waiting_for_status)

    async def habit_get_status(self, message: Message, state: FSMContext):
        status = "active" if message.text == "Now" else "pause"
        await state.update_data(status=status)

        data = await state.get_data()
        summary = (
            f"<b>Check data:</b>\n"
            f"Name: {data['name']}\n"
            f"Time: {data['time_notification']}\n"
            f"Status: {data['status']}"
        )

        await message.answer(summary, reply_markup=confirm_habit_kb)
        await state.set_state(AddHabitStates.waiting_for_confirmation)

    async def habit_confirmation(self, message: Message, state: FSMContext):
        text = message.text
        data = await state.get_data()

        if text == "Save":
            
            username = message.from_user.username
            user_id = message.from_user.id
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.repository.add_habit(
                username=username,
                user_id=user_id,
                name=data['name'],
                time_notification=data['time_notification'],
                status=data['status']
            )

            await message.answer("Habit saved", reply_markup=habits_menu)
            await state.clear()

        if text == "Edit":
            await message.answer("Get start again! Write habit name: ")
            await state.set_state(AddHabitStates.waiting_for_name)
        
        elif text == "Cancel":
            await message.answer("Create habit cancel", reply_markup=habits_menu)

        else:
            await message.answer("Please choose action with buttons")
