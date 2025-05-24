import logging
from aiogram import Router, F
from aiogram.types import Message

from main_keyboards import main_menu
from features.games.keyboards import games_menu
from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu, games_irregular_verbs_choose_level
from features.games.irregular_verbs.repo import IrregularVerbsRepository
from features.games.irregular_verbs.service import IrregularVerbsGame


class HandlerLevelGameIrregularVerbs:
    def __init__(self):
        self.router = Router()
        self.db = IrregularVerbsRepository()
        self.game = IrregularVerbsGame(self.db)

        # Выбор уровня — без фильтров
        self.router.message.register(self.start_play_easy_irregular_verbs, F.text.lower() == "easy")
        self.router.message.register(self.start_play_medium_irregular_verbs, F.text.lower() == "medium")
        self.router.message.register(self.start_play_hard_irregular_verbs, F.text.lower() == "hard")

        # Ответы игрока — фильтр is_in_game
        self.router.message.register(self.check_answer, lambda msg: self.is_in_game(msg))

        # Назад в меню игры
        self.router.message.register(self.back_to_the_game_menu, F.text.lower() == "exit level selection menu")

        # Отладочный fallback — для всего, что не обработалось
        @self.router.message()
        async def fallback_debug_handler(message: Message):
            logging.debug(f"[FALLBACK] Необработанное сообщение: {message.text}")


    async def start_play_easy_irregular_verbs(self, message: Message):
        logging.debug(f"[GAME] Нажата кнопка Easy от @{message.from_user.username}")
        await self.game.start_game(message, level="Easy")

    async def start_play_medium_irregular_verbs(self, message: Message):
        logging.debug(f"[GAME] Нажата кнопка Medium от @{message.from_user.username}")
        await self.game.start_game(message, level="Medium")

    async def start_play_hard_irregular_verbs(self, message: Message):
        logging.debug(f"[GAME] Нажата кнопка Hard от @{message.from_user.username}")
        await self.game.start_game(message, level="Hard")

    async def check_answer(self, message: Message):
        logging.debug(f"[ANSWER] Пользователь @{message.from_user.username} ответил: {message.text}")
        await self.game.check_answer(message)

    async def back_to_the_game_menu(self, message: Message):
        logging.debug(f"[BACK] Пользователь @{message.from_user.username} вернулся в меню игры")
        await message.answer('Go to the game menu', reply_markup=games_irregular_verbs_menu)

    def is_in_game(self, message: Message) -> bool:
        user_id = message.from_user.id
        state = self.game.user_states.get(user_id)
        in_game = state is not None and state.get("in_game", False)
        logging.debug(f"[STATE] is_in_game={in_game} for user_id={user_id}")
        return in_game
