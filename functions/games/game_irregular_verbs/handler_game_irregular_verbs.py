from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from functions.games.keyboards_games import games_menu
from functions.games.game_irregular_verbs.keyboard_game_irregular_verbs import games_irregular_verbs_menu, games_irregular_verbs_choose_level
from functions.games.game_irregular_verbs.game_irregular_verbs_service import IrregularVerbsGame, IrregularVerbsRepository

class HandlerGameIrregularVerbs():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.start_play_irregular_verbs, lambda message: message.text == "Play")
        self.router.message.register(self.statistics_irregular_verbs, lambda message: message.text == "Statistics")
        self.router.message.register(self.rules_irregular_verbs, lambda message: message.text == "Rules")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    
    async def start_play_irregular_verbs(self, message: Message):
        await message.answer("Choose the level for game", reply_markup=games_irregular_verbs_choose_level)

    async def statistics_irregular_verbs(self, message: Message):
        await message.answer("Statistics in progress", reply_markup=games_irregular_verbs_menu)

    async def rules_irregular_verbs(self, message: Message):
        # await message.answer("Rules in progress", reply_markup=games_irregular_verbs_menu) #заглушка до окончания разработки
        await message.answer(
            "🎮 *Game: Irregular Verbs*\n"
            "This game helps you learn and reinforce irregular verbs in English.\n\n"
            "🔹 *3 difficulty levels:*\n"
            "1. *Easy* – translate from Russian to English (infinitive only, V1)\n"
            "2. *Medium* – V1 + past simple (V2)\n"
            "3. *Hard* – V1 + V2 + past participle (V3)\n\n"
            "💬 *How to answer:*\n"
            "- One word per message\n"
            "- On Medium and Hard levels, the bot will guide you\n",
            parse_mode="Markdown", reply_markup=games_irregular_verbs_menu)
    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)


class HandlerLevelGameIrregularVerbs():
    def __init__(self):
        self.router = Router()
        self.db = IrregularVerbsRepository("sql_lite/irregular_verbs.db")
        self.game = IrregularVerbsGame(self.db)

        # Выбор уровня
        self.router.message.register(self.start_play_easy_irregular_verbs, lambda message: message.text == "Easy")
        self.router.message.register(self.start_play_medium_irregular_verbs, lambda message: message.text == "Medium")
        self.router.message.register(self.start_play_hard_irregular_verbs, lambda message: message.text == "Hard")

        # Ответы игрока
        self.router.message.register(self.check_answer, self.is_in_game)

        # Назад
        self.router.message.register(self.back_to_the_game_menu, lambda message: message.text == "Go back")

    async def start_play_easy_irregular_verbs(self, message: Message):
        await self.game.start_game(message, level="Easy")

    async def start_play_medium_irregular_verbs(self, message: Message):
        await self.game.start_game(message, level="Medium")

    async def start_play_hard_irregular_verbs(self, message: Message):
        await self.game.start_game(message, level="Hard")

    async def check_answer(self, message: Message):
        await self.game.check_answer(message)

    async def back_to_the_game_menu(self, message: Message):
        await message.answer('Go to the game menu', reply_markup=games_irregular_verbs_menu)

    def is_in_game(self, message: Message) -> bool:
        """Фильтр: обрабатывать сообщение как ответ, если пользователь в игре"""
        user_id = message.from_user.id
        state = self.game.user_states.get(user_id)
        return state is not None and state.get("in_game", False)

# from aiogram import Router
# from aiogram.types import Message
# from main_keyboards import main_menu
# from functions.games.keyboards_games import games_menu
# from functions.games.game_irregular_verbs.keyboard_game_irregular_verbs import games_irregular_verbs_menu, games_irregular_verbs_choose_level
# from functions.games.game_irregular_verbs.game_irregular_verbs_service import IrregularVerbsGame, IrregularVerbsRepository

# class HandlerGameIrregularVerbs():
#     def __init__(self):
#         self.router = Router()

#         self.router.message.register(self.start_play_irregular_verbs, lambda message: message.text == "Play")
#         self.router.message.register(self.statistics_irregular_verbs, lambda message: message.text == "Statistics")
#         self.router.message.register(self.rules_irregular_verbs, lambda message: message.text == "Rules")
#         self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    
#     async def start_play_irregular_verbs(self, message: Message):
#         await message.answer("Choose the level for game", reply_markup=games_irregular_verbs_choose_level)

#     async def statistics_irregular_verbs(self, message: Message):
#         await message.answer("Statistics in progress", reply_markup=games_irregular_verbs_menu)

#     async def rules_irregular_verbs(self, message: Message):
#         await message.answer("Rules in progress", reply_markup=games_irregular_verbs_menu)
    
#     async def back_main_menu_handler(self, message: Message):
#         await message.answer('Go to main menu', reply_markup=main_menu)


# class HandlerLevelGameIrregularVerbs():
#     def __init__(self):
#         self.router = Router()
#         self.db = IrregularVerbsRepository("sql_lite/irregular_verbs.db")
#         self.game = IrregularVerbsGame(self.db)

#         self.router.message.register(self.start_play_easy_irregular_verbs, lambda message: message.text == "Easy")
#         self.router.message.register(self.start_play_medium_irregular_verbs, lambda message: message.text == "Medium")
#         self.router.message.register(self.start_play_hard_irregular_verbs, lambda message: message.text == "Hard")
        
#         self.router.message.register(self.back_to_the_game_menu, lambda message: message.text == "Go back")
#         self.router.message.register(self.check_answer, lambda message: True) # проверка любых ответов - потом убрать из проверки выбор уровня и кнопку назад

#     async def start_play_easy_irregular_verbs(self, message: Message):
#         # await message.answer('Easy in progress', reply_markup=games_irregular_verbs_choose_level)
#         await self.game.start_game(message, level="Easy")

#     async def start_play_medium_irregular_verbs(self, message: Message):
#         await message.answer('Medium in progress', reply_markup=games_irregular_verbs_choose_level)

#     async def start_play_hard_irregular_verbs(self, message: Message):
#         await message.answer('Hard in progress', reply_markup=games_irregular_verbs_choose_level)

#     async def check_answer(self, message: Message):
#         await self.game.check_answer(message)

#     async def back_to_the_game_menu(self, message: Message):
#         await message.answer('Go to the game menu', reply_markup=games_irregular_verbs_menu)


