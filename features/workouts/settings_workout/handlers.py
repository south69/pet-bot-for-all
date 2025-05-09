from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from features.workouts.keyboards import workouts_menu
from features.workouts.settings_workout.keyboards import settings_workout_menu, trainings_workout_menu, exercise_workout_menu


class HandlerSettingsWorkout():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.settings_workout_trainings_handler, lambda message: message.text == "Trainings")
        self.router.message.register(self.settings_workout_exercise_handler, lambda message: message.text == "Exercise")
        self.router.message.register(self.settings_workout_go_back_handler, lambda message: message.text =="Go back")

    
    async def settings_workout_trainings_handler(self, message: Message):
        await message.answer("Go to settings training (in progress)", reply_markup=trainings_workout_menu)

    async def settings_workout_exercise_handler(self, message: Message):
        await message.answer("Go to settings exercise (in progress)", reply_markup=exercise_workout_menu)

    async def settings_workout_go_back_handler(self, message: Message):
        await message.answer("Go back to workouts menu", reply_markup=workouts_menu)


class HandlerTrainingsWorkoutMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.show_trainings_handler,lambda message: message.text == "Show trainings")
        self.router.message.register(self.edit_trainings_handler,lambda message: message.text == "Edit trainings")
        self.router.message.register(self.delete_trainings_handler,lambda message: message.text == "Delete trainings")
        self.router.message.register(self.go_back_trainings_handler,lambda message: message.text == "Go back")

    async def show_trainings_handler(self, message: Message):
        await message.answer("Go to show training (in progress)", reply_markup=trainings_workout_menu)

    async def edit_trainings_handler(self, message: Message):
        await message.answer("Go to edit training (in progress)", reply_markup=trainings_workout_menu)

    async def delete_trainings_handler(self, message: Message):
        await message.answer("Go to delete training (in progress)", reply_markup=trainings_workout_menu)

    async def go_back_trainings_handler(self, message: Message):
        await message.answer("Go back to settings menu", reply_markup=settings_workout_menu)


class HandlerExerciseWorkoutMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.show_exercise_handler,lambda message: message.text == "Show exercise")
        self.router.message.register(self.edit_exercise_handler,lambda message: message.text == "Edit exercise")
        self.router.message.register(self.delete_exercise_handler,lambda message: message.text == "Delete exercise")
        self.router.message.register(self.go_back_exercise_handler,lambda message: message.text == "Go back")

    async def show_exercise_handler(self, message: Message):
        await message.answer("Go to show exercise (in progress)", reply_markup=exercise_workout_menu)

    async def edit_exercise_handler(self, message: Message):
        await message.answer("Go to edit exercise (in progress)", reply_markup=exercise_workout_menu)

    async def delete_exercise_handler(self, message: Message):
        await message.answer("Go to delete exercise (in progress)", reply_markup=exercise_workout_menu)

    async def go_back_exercise_handler(self, message: Message):
        await message.answer("Go back to settings menu", reply_markup=settings_workout_menu)


