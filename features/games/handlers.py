from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from features.games.keyboards import games_menu
from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu

class HandlerGamesMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.game_irregular_verbs_handler, lambda message: message.text == "Irregular verbs (English)")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    
    async def game_irregular_verbs_handler(self, message: Message):
        await message.answer("Go to game Irregular Verbs!", reply_markup=games_irregular_verbs_menu)
    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)
