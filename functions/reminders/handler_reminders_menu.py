from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from functions.reminders.keyboards_reminders import reminders_menu

class HandlerRemindersMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.add_habit_handler, lambda message: message.text == "Add remind")
        self.router.message.register(self.change_habit_handler, lambda message: message.text == "Change remind")
        self.router.message.register(self.delete_habit_handler, lambda message: message.text == "Delete remind")
        self.router.message.register(self.show_my_habits_handler, lambda message: message.text == "Show my reminders")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    
    async def add_habit_handler(self, message: Message):
        await message.answer("Feature in development", reply_markup=reminders_menu)

    async def change_habit_handler(self, message: Message):
        await message.answer("Feature in development", reply_markup=reminders_menu)

    async def delete_habit_handler(self, message: Message):
        await message.answer("Feature in development", reply_markup=reminders_menu)

    async def show_my_habits_handler(self, message: Message):
        await message.answer("Feature in development", reply_markup=reminders_menu)

    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)



