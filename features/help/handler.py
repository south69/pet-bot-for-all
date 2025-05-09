from aiogram import Router
from aiogram.types import Message
from main_keyboards import main_menu
from features.help.keyboards import help_menu

class HandlerHelpMenu():
    def __init__(self):
        self.router = Router()

        self.router.message.register(self.about_bot_handler, lambda message: message.text == "About Bot")
        self.router.message.register(self.suggest_update_handler, lambda message: message.text == "Suggest update")
        self.router.message.register(self.bug_report_handler, lambda message: message.text == "Bug report")
        self.router.message.register(self.ask_developer_handler, lambda message: message.text == "Ask developer")
        self.router.message.register(self.back_main_menu_handler, lambda message: message.text =="Back main menu")

    
    async def about_bot_handler(self, message: Message):
        await message.answer(
            "I'm a helper bot created to assist those who know about me.\n"
            "You can find more details about me on \n"
            "<a href='https://github.com/south69/pet-bot-for-all'>GitHub Repository</a>",
            reply_markup=help_menu,
            parse_mode="HTML"
            )
    
    async def suggest_update_handler(self, message: Message):
        await message.answer('Please contact @south_dev', reply_markup=help_menu)

    async def bug_report_handler(self, message: Message):
        await message.answer('Please contact @south_dev', reply_markup=help_menu)

    async def ask_developer_handler(self, message: Message):
        await message.answer('Please contact @south_dev', reply_markup=help_menu)
    
    async def back_main_menu_handler(self, message: Message):
        await message.answer('Go to main menu', reply_markup=main_menu)



