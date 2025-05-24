from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime

import logging

from main_keyboards import main_menu
from features.habits.keyboards import habits_menu, confirm_habit_kb, status_choise_kb, did_i_know_id_habit, confirm_delete_habit_kb
from features.habits.repo import HabitsRepository

from features.habits.handlers.add_habit import HandlerAddHabit
from features.habits.handlers.change_habit import HandlerChangeHabit
from features.habits.handlers.show_my_habit import HandlerShowHabit
from features.habits.handlers.delete_habit import HandlerDeleteHabit

print('✅ handler_habits_menu вызван до начала отработки класса')

# ✅__Главное меню привычек__
class HandlerHabitsMenu():
    def __init__(self):
        print('✅ Habits - Handler. HandlerHabitsMenu инициирован')
        self.router = Router()
        self.repo = HabitsRepository()

        # Подключаю вложенные роутеры
        self.router.include_router(HandlerAddHabit(repository=self.repo).router)
        self.router.include_router(HandlerChangeHabit(repository=self.repo).router)
        self.router.include_router(HandlerShowHabit(repository=self.repo).router)
        self.router.include_router(HandlerDeleteHabit(repository=self.repo).router)

        # Кнопка "Назад"
        self.router.message.register(self.back_main_menu_handler_for_habits, lambda message: message.text =="Exit habits")

    async def back_main_menu_handler_for_habits(self, message):
        await message.answer("Go to main menu", reply_markup=main_menu)

        
    # def __init__(self):
    #     self.router = Router()
    #     self.db = HabitsRepository()

    #     # Подтягиваю все кнопки
    #     self.router.message.register(self.add_habit_handler, F.text == "Add habit")
    #     self.router.message.register(self.change_habit_handler, F.text == "Change habit")
    #     self.router.message.register(self.show_habit_handler, F.text == "Show my habits")
    #     self.router.message.register(self.delete_habit_handler, F.text == "Delete habit")
    #     self.router.message.register(self.back_main_menu_habit_handler, F.text == "Back main menu")

    #     # Отладочный fallback — для всего, что не обработалось
    #     @self.router.message()
    #     async def fallback_debug_handler(message: Message):
    #         logging.debug(f"[FALLBACK] Необработанное сообщение: {message.text}")

    # async def add_habit_handler(self, message: Message):
    #     await message.answer("'Add habit - coming soon...'", reply_markup=habits_menu)

    # async def change_habit_handler(self, message: Message):
    #     await message.answer("'Change habit - coming soon...'", reply_markup=habits_menu)

    # async def show_habit_handler(self, message: Message):
    #     await message.answer("'Show habit - coming soon...'", reply_markup=habits_menu)

    # async def delete_habit_handler(self, message: Message):
    #     await message.answer("'Delete habit - coming soon...'", reply_markup=habits_menu)

    # async def back_main_menu_habit_handler(self, message: Message):
    #     await message.answer("Back main menu habit", reply_markup=main_menu)

# -----------------------


    # def __init__(self):
    #     print('✅ Habits - Handler. HandlerHabitsMenu инициирован')
    #     self.router = Router()
    #     self.repo = HabitsRepository()

    #     # Подключаю вложенные роутеры
    #     self.router.include_router(HandlerAddHabit(repository=self.repo).router)
    #     self.router.include_router(HandlerChangeHabit(repository=self.repo).router)
    #     self.router.include_router(HandlerShowHabit(repository=self.repo).router)
    #     self.router.include_router(HandlerDeleteHabit(repository=self.repo).router)

    #     # Кнопка "Назад"
    #     self.router.message.register(self.back_main_menu_handler_for_habits, lambda message: message.text =="Back main menu")

    # async def back_main_menu_handler_for_habits(self, message):
    #     await message.answer("Go to main menu", reply_markup=main_menu)
# ------------------------------------------------------------------

# import logging
# from aiogram import Router, F
# from aiogram.types import Message

# from main_keyboards import main_menu
# from features.games.keyboards import games_menu
# from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu, games_irregular_verbs_choose_level
# from features.games.irregular_verbs.repo import IrregularVerbsRepository
# from features.games.irregular_verbs.service import IrregularVerbsGame


# class HandlerLevelGameIrregularVerbs:
#     def __init__(self):
#         self.router = Router()
#         self.db = IrregularVerbsRepository()
#         self.game = IrregularVerbsGame(self.db)

#         # Выбор уровня — без фильтров
#         self.router.message.register(self.start_play_easy_irregular_verbs, F.text.lower() == "easy")
#         self.router.message.register(self.start_play_medium_irregular_verbs, F.text.lower() == "medium")
#         self.router.message.register(self.start_play_hard_irregular_verbs, F.text.lower() == "hard")

#         # Ответы игрока — фильтр is_in_game
#         self.router.message.register(self.check_answer, lambda msg: self.is_in_game(msg))

#         # Назад в меню игры
#         self.router.message.register(self.back_to_the_game_menu, F.text.lower() == "go back to the game")

#         # Отладочный fallback — для всего, что не обработалось
#         @self.router.message()
#         async def fallback_debug_handler(message: Message):
#             logging.debug(f"[FALLBACK] Необработанное сообщение: {message.text}")


#     async def back_to_the_game_menu(self, message: Message):
#         logging.debug(f"[BACK] Пользователь @{message.from_user.username} вернулся в меню игры")
#         await message.answer('Go to the game menu', reply_markup=games_irregular_verbs_menu)




    # async def start_play_easy_irregular_verbs(self, message: Message):
    #     logging.debug(f"[GAME] Нажата кнопка Easy от @{message.from_user.username}")
    #     await self.game.start_game(message, level="Easy")

    # async def start_play_medium_irregular_verbs(self, message: Message):
    #     logging.debug(f"[GAME] Нажата кнопка Medium от @{message.from_user.username}")
    #     await self.game.start_game(message, level="Medium")

    # async def start_play_hard_irregular_verbs(self, message: Message):
    #     logging.debug(f"[GAME] Нажата кнопка Hard от @{message.from_user.username}")
    #     await self.game.start_game(message, level="Hard")

    # async def check_answer(self, message: Message):
    #     logging.debug(f"[ANSWER] Пользователь @{message.from_user.username} ответил: {message.text}")
    #     await self.game.check_answer(message)

    # async def back_to_the_game_menu(self, message: Message):
    #     logging.debug(f"[BACK] Пользователь @{message.from_user.username} вернулся в меню игры")
    #     await message.answer('Go to the game menu', reply_markup=games_irregular_verbs_menu)

    # def is_in_game(self, message: Message) -> bool:
    #     user_id = message.from_user.id
    #     state = self.game.user_states.get(user_id)
    #     in_game = state is not None and state.get("in_game", False)
    #     logging.debug(f"[STATE] is_in_game={in_game} for user_id={user_id}")
    #     return in_game
