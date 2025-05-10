from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

from main_keyboards import main_menu
from features.habits.keyboards import habits_menu, confirm_habit_kb, status_choise_kb, did_i_know_id_habit, confirm_delete_habit_kb
from features.habits.repo import HabitsRepository
from features.habits.states import AddHabitStates, DeleteHabitStatuses

# __Главное меню привычек__
class HandlerHabitsMenu():
    def __init__(self):
        self.router = Router()

        repo = HabitsRepository()
        add_habit = HandlerAddHabit(repository=repo)
        change_habit = HandlerChangeHabit(repository=repo)
        show_habit = HandlerShowHabit(repository=repo)
        delete_habit = HandlerDeleteHabit(repository=repo)

        self.router.include_router(add_habit.router)
        self.router.include_router(change_habit.router)
        self.router.include_router(show_habit.router)
        self.router.include_router(delete_habit.router)

        # self.router.message.register(self.add_habit_handler, lambda message: message.text == "Add habit")
        # self.router.message.register(self.change_habit_handler, lambda message: message.text == "Change habit")
        # self.router.message.register(self.delete_habit_handler, lambda message: message.text == "Delete habit")
        # self.router.message.register(self.show_my_habits_handler, lambda message: message.text == "Show my habits")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    # async def add_habit_handler(self, message: Message):
    #     await message.answer("In progress", reply_markup=habits_menu)

    # async def change_habit_handler(self, message: Message):
    #     await message.answer("In progress", reply_markup=habits_menu)

    # async def delete_habit_handler(self, message: Message):
    #     await message.answer("In progress", reply_markup=habits_menu)

    # async def show_my_habits_handler(self, message: Message):
    #     await message.answer("In progress", reply_markup=habits_menu)

    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)


# __Добавление привычки__ add_habit
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
        await message.answer("Please enter the name of the habit", reply_markup=ReplyKeyboardRemove())
        await state.set_state(AddHabitStates.waiting_for_name)

    async def habit_get_name(self, message: Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer("Choose a time, like 08:00")
        await state.set_state(AddHabitStates.waiting_for_time)

    async def habit_get_time(self, message: Message, state: FSMContext):
        await state.update_data(time_notification=message.text)
        await message.answer("Would you like to activate it now or later?", reply_markup=status_choise_kb)
        await state.set_state(AddHabitStates.waiting_for_status)

    async def habit_get_status(self, message: Message, state: FSMContext):
        status = "active" if message.text == "Now" else "pause"
        await state.update_data(status=status)

        data = await state.get_data()
        summary = (
            f"<b>Please confirm the details:</b>\n"
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

            await message.answer("Habit has been saved", reply_markup=habits_menu)
            await state.clear()

        if text == "Edit":
            await message.answer("Get start again! Please enter the name of the habit: ")
            await state.set_state(AddHabitStates.waiting_for_name)
        
        elif text == "Cancel":
            await message.answer("Habit creaton cancelled", reply_markup=habits_menu)

        else:
            await message.answer("Please choose action with buttons")

# !!!__Изменение привычки__ change_habit
class HandlerChangeHabit:
    def __init__(self, repository: HabitsRepository):
        self.router = Router()
        self.repository = repository
        self._register_handlers()

    def _register_handlers(self):

        self.router.message.register(self.cancel_delete_habit, F.text == "Cancel")

# !!!__Просмотр привычки__ show_habit
class HandlerShowHabit:
    def __init__(self, repository: HabitsRepository):
        self.router = Router()
        self.repository = repository
        self._register_handlers()

    def _register_handlers(self):
        self.router.message.register(self.show_ne_habits_handler, F.text == "Show my habits")
        self.router.message.register(self.cancel_delete_habit, F.text == "Cancel")

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

# !!!__Удаление привычки__ delete_habit
class HandlerDeleteHabit:
    def __init__(self, repository: HabitsRepository):
        self.router = Router()
        self.repository = repository
        self._register_handlers()

    def _register_handlers(self):

        self.router.message.register(self.cancel_delete_habit, F.text == "Cancel")

        self.router.message.register(self.start_delete_habit, F.text == "Delete habit")
        self.router.message.register(self.habit_get_id_for_delete, DeleteHabitStatuses.waiting_for_id)
        self.router.message.register(self.habit__delete_confirmation, DeleteHabitStatuses.waiting_for_confirmation)

    async def cancel_delete_habit(self, message: Message, state: FSMContext):
        await state.clear()
        await message.answer("Habit deletion cancelled", reply_markup=habits_menu)

    async def start_delete_habit(self, message: Message, state: FSMContext):
        await message.answer("Please enter id of the habit", reply_markup=ReplyKeyboardRemove())
        await state.set_state(DeleteHabitStatuses.waiting_for_id)
    

        

