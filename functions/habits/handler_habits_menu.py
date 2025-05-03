from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from functions.habits.keyboards_habits import habits_menu
from sql_lite.habits_repository import HabitsRepository
from functions.habits.handler_add_habit import HandlerAddHabit

class HandlerHabitsMenu():
    def __init__(self):
        self.router = Router()

        repo = HabitsRepository(db_path="sql_lite/habits.db")
        add_habit = HandlerAddHabit(repository=repo)
        self.router.include_router(add_habit.router)

        # self.router.message.register(self.add_habit_handler, lambda message: message.text == "Add habit")
        self.router.message.register(self.change_habit_handler, lambda message: message.text == "Change habit")
        self.router.message.register(self.delete_habit_handler, lambda message: message.text == "Delete habit")
        self.router.message.register(self.show_my_habits_handler, lambda message: message.text == "Show my habits")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    # async def add_habit_handler(self, message: Message):
    #     await message.answer("In progress", reply_markup=habits_menu)

    async def change_habit_handler(self, message: Message):
        await message.answer("In progress", reply_markup=habits_menu)

    async def delete_habit_handler(self, message: Message):
        await message.answer("In progress", reply_markup=habits_menu)

    async def show_my_habits_handler(self, message: Message):
        await message.answer("In progress", reply_markup=habits_menu)

    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)



