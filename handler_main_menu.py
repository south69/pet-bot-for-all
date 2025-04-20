from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu

from functions.reminders.keyboards_reminders import reminders_menu
from functions.habits.keyboards_habits import habits_menu
from functions.games.keyboards_games import games_menu
from functions.workouts.keyboards_workouts import workouts_menu
from functions.help.keyboards_help import help_menu


class HandlerMainMenu:
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.reminders_handler, lambda message: message.text == "Reminders")
        self.router.message.register(self.habits_handler, lambda message: message.text == "Habits")
        self.router.message.register(self.games_handler, lambda message: message.text == "Games")
        self.router.message.register(self.workouts_handler, lambda message: message.text == 'Workouts')
        self.router.message.register(self.help_handler, lambda message: message.text == "Help")

    async def reminders_handler(self, message: Message):    
        await message.answer('Go to Reminders', reply_markup=reminders_menu)

    async def habits_handler(self, message: Message):
        await message.answer('Go to Habits', reply_markup=habits_menu)

    async def games_handler(self, message: Message):
        await message.answer('Go to Games', reply_markup=games_menu)

    async def workouts_handler(self, message: Message):
        await message.answer('Go to Workouts', reply_markup=workouts_menu)

    async def help_handler(self, message: Message):
        await message.answer('Go to Help', reply_markup=help_menu)