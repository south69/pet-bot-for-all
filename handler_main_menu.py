from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from main_keyboards import main_menu
from main_states import MainStates

from features.reminders.keyboards import reminders_menu
from features.habits.keyboards import habits_menu
from features.games.keyboards import games_menu
from features.workouts.keyboards import workouts_menu
from features.help.keyboards import help_menu


class HandlerMainMenu:
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.start_handler, CommandStart())

        self.router.message.register(self.reminders_handler, lambda message: message.text == "🛠 Reminders")
        self.router.message.register(self.habits_handler, lambda message: message.text == "🛠 Habits")
        self.router.message.register(self.games_handler, lambda message: message.text == "🎮 Games")
        self.router.message.register(self.workouts_handler, lambda message: message.text == '🛠 Workouts')
        self.router.message.register(self.help_handler, lambda message: message.text == "🧙‍♂️ Help")

    async def start_handler(self, message:Message):
        await message.answer(
            f"Hi, {message.from_user.username}! I'm your bot assist for all. How can I help you today?", reply_markup=main_menu
        )

    async def reminders_handler(self, message: Message):    
        await message.answer('Go to Reminders', reply_markup=reminders_menu)

    async def habits_handler(self, message: Message):
        await message.answer('Go to Habits', reply_markup=habits_menu)

    async def games_handler(self, message: Message, state: FSMContext):
        await state.set_state(MainStates.in_games)
        await message.answer('Go to Games', reply_markup=games_menu)

    async def workouts_handler(self, message: Message):
        await message.answer('Go to Workouts', reply_markup=workouts_menu)

    async def help_handler(self, message: Message, state: FSMContext):
        await state.set_state(MainStates.in_help)
        await message.answer('Go to Help', reply_markup=help_menu)