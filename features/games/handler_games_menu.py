from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from main_keyboards import main_menu
from features.games.keyboards import games_menu
from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu
from main_states import MainStates

class HandlerGamesMenu:
    def __init__(self):
        self.router = Router(name="games")

        # Используем состояние MainStates.in_games
        self.router.message.register(self.game_irregular_verbs_handler,MainStates.in_games, F.text == "Irregular verbs")
        self.router.message.register(self.back_main_menu_handler,MainStates.in_games, F.text == "Exit games")

    async def game_irregular_verbs_handler(self, message: Message, state: FSMContext):
        await message.answer("Go to game Irregular Verbs!", reply_markup=games_irregular_verbs_menu)

    async def back_main_menu_handler(self, message: Message, state: FSMContext):
        await state.set_state(MainStates.in_main_menu)
        await message.answer("Back to main menu", reply_markup=main_menu)
