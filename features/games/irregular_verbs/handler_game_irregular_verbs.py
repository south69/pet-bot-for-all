from aiogram import Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram import F

# from main_keyboards import main_menu
from features.games.keyboards import games_menu
from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu, games_irregular_verbs_choose_level, stats_period_kb
from features.games.irregular_verbs.repo import IrregularVerbsRepository

import matplotlib.pyplot as plt
from io import BytesIO
from functools import partial


class HandlerGameIrregularVerbs():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.start_play_irregular_verbs, lambda message: message.text == "Play")
        self.router.message.register(self.statistics_irregular_verbs, lambda message: message.text == "Statistics")
        self.router.message.register(self.rules_irregular_verbs, lambda message: message.text == "Rules")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back to games menu")

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
        ax.set_ylim(0, 100)

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

    async def rules_irregular_verbs(self, message: Message):
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
        await message.answer('Go to main menu', reply_markup=games_menu)




