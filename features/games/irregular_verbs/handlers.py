from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram import F

from main_keyboards import main_menu
from features.games.keyboards import games_menu
from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu, games_irregular_verbs_choose_level, stats_period_kb
from features.games.irregular_verbs.service import IrregularVerbsGame, IrregularVerbsRepository

import matplotlib.pyplot as plt
from io import BytesIO


class HandlerGameIrregularVerbs():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.start_play_irregular_verbs, lambda message: message.text == "Play")
        self.router.message.register(self.statistics_irregular_verbs, lambda message: message.text == "Statistics")
        self.router.message.register(self.rules_irregular_verbs, lambda message: message.text == "Rules")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

        self.router.callback_query.register(self.show_statistics_period, lambda c: c.data.startswith("stats:"))
    
    async def start_play_irregular_verbs(self, message: Message):
        await message.answer("Choose the level for game", reply_markup=games_irregular_verbs_choose_level)

    async def statistics_irregular_verbs(self, message: Message):
        await message.answer("Choose period:", reply_markup=stats_period_kb)

    async def show_statistics_period(self, callback: CallbackQuery):
        period = callback.data.split(":")[1]
        repo = IrregularVerbsRepository()
        stats = repo.get_user_statistics(callback.from_user.id, period=period)
        repo.close()

        if not stats:
            await callback.message.edit_text("No statistics available for this period")
            return

        lines = [f"Statistics: *{period.upper()}*"]
        for level, total, correct, percent in stats:
            lines.append(f"• *{level}*: {correct}/{total} correct ({percent}%)")

        # Построение графика
        levels = [level for level, total, correct, percent in stats]
        percents = [percent for level, total, correct, perctnt in stats]

        fig, ax = plt.subplots()
        ax.bar(levels, percents, color='skyblue')
        ax.set_title(f"Correct answers by level ({period.capitalize()})")
        ax.set_ylabel("Correct answers (%)")
        ax.set.ylim(0, 100)

        # Сохранение графика в буффер обмена
        buf = BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)

        # Отправка графика
        image = BufferedInputFile(buf.read(), filename="stats.png")
        await callback.message.answer_photo(
            image,
            caption="\n".join(lines),
            parse_mode="Markdown"
        )



        # await callback.message.edit_text("\n".join(lines), parse_mode="Markdown")

        # await message.answer("Statistics in progress", reply_markup=games_irregular_verbs_menu)

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
        self.db = IrregularVerbsRepository()
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

