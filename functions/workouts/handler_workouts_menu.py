from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from functions.workouts.keyboards_workouts import workouts_menu
from functions.workouts.settings_workout.keyboards_settings_workout import settings_workout_menu
from functions.workouts.start_workout.keyboards_start_workout import start_workout_choose_menu

class HandlerWorkoutsMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.start_workouts_handler, lambda message: message.text == "Start")
        self.router.message.register(self.progress_workouts_handler, lambda message: message.text == "Progress")
        self.router.message.register(self.settings_workouts_handler, lambda message: message.text == "Settings")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    
    async def start_workouts_handler(self, message: Message):
        await message.answer("Go to choose a training", reply_markup=start_workout_choose_menu)

    async def progress_workouts_handler(self, message: Message):
        await message.answer("In progress", reply_markup=workouts_menu)

    async def settings_workouts_handler(self, message: Message):
        await message.answer("Go to settings workout", reply_markup=settings_workout_menu)
    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)

