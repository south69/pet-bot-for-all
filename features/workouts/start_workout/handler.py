from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from features.workouts.keyboards import workouts_menu
from features.workouts.start_workout.keyboards import start_workout_choose_menu


class HandlerStartWorkoutMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.select_training, lambda message: message.text == "Select training")
        self.router.message.register(self.choose_training, lambda message: message.text == "Choose training")
        self.router.message.register(self.start_workout_go_back, lambda message: message.text =="Go back to workouts menu")

    
    async def select_training(self, message: Message):
        await message.answer("Go to select training (in progress)", reply_markup=start_workout_choose_menu)

    async def choose_training(self, message: Message):
        await message.answer("Go to settings exercise (in progress)", reply_markup=start_workout_choose_menu)

    async def start_workout_go_back(self, message: Message):
        await message.answer("Go back to workouts menu", reply_markup=workouts_menu)


 