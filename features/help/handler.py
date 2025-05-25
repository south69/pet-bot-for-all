from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from main_keyboards import main_menu
from features.help.keyboards import help_menu
from main_states import MainStates

class HandlerHelpMenu():
    def __init__(self):
        self.router = Router(name="help")

        self.router.message.register(self.about_bot_handler, MainStates.in_help, F.text == "About Bot")
        self.router.message.register(self.suggest_update_handler, MainStates.in_help, F.text == "Suggest update")
        self.router.message.register(self.bug_report_handler, MainStates.in_help, F.text == "Bug report")
        self.router.message.register(self.ask_developer_handler, MainStates.in_help, F.text == "Ask developer")
        self.router.message.register(self.back_main_menu_handler, MainStates.in_help, F.text == "Exit help")

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

    async def back_main_menu_handler(self, message: Message, state: FSMContext):
        await state.set_state(MainStates.in_main_menu)
        await message.answer('Back to main menu', reply_markup=main_menu)
