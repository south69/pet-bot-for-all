from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

import psycopg2
import os
from config import POSTGRES_URL
from functions.games.game_irregular_verbs.keyboard_game_irregular_verbs import games_irregular_verbs_menu, games_irregular_verbs_choose_level
from functions.games.game_irregular_verbs.irregular_verbs_repository import IrregularVerbsRepository

class IrregularVerbsGame:
    def __init__(self, db: IrregularVerbsRepository):
        self.db = db
        self.user_states = {}

        self.session_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Go back"), KeyboardButton(text="Don't know")]
            ],
            resize_keyboard=True
        )

    async def start_game(self, message: Message, level: str):
        user_id = message.from_user.id
        verb = self.db.get_random_verb()

        if not verb:
            print('Connection to DB is lost. Try again later')
            return
        
        self.user_states[user_id] = {
            "in_game": True,
            "verb" : verb,
            "level": level,
            "step": 0,
            "answers": []
        }

        await self.ask_next_step(message, user_id)

    async def ask_next_step(self, message: Message, user_id: int):
        state = self.user_states[user_id]
        step = state["step"]
        level = state["level"]
        translate = state["verb"]["translate"]

        prompts = {
            0: "infinitive",
            1: "past_simple_v2",
            2: "past_participle_v3"
        }

        await message.answer(
            f"Translate: <b>{translate}</b>\nEnter the {prompts[step]} form: ",
            reply_markup=self.session_keyboard
        )
        
    async def check_answer(self, message: Message):
        user_id = message.from_user.id
        state = self.user_states.get(user_id)

        if not state or not state.get("in_game"):
            await message.answer("Start a new game. Choose level!")
            return
        
        user_input  = message.text.strip().lower()

        if user_input  == "go back":
            state["in_game"] = False
            await message.answer(
                "You've left the game. Choose level again",
                reply_markup=games_irregular_verbs_choose_level
            )
            return
        
        if user_input  == "don't know":
            await self.send_correct_answer(message, state)
            await self.start_game(message, state["level"])
            return

        level = state["level"]
        expected_steps = {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3
        }[level]

        state["answers"].append(user_input)
        state["step"] += 1

        if state["step"] < expected_steps:
            await self.ask_next_step(message, user_id)
            return
        
        verb = state["verb"]
        correct = [
            verb["infinitive"].lower(),
            verb["past_simple_v2"].lower(),
            verb["past_participle_v3"].lower()
        ][:expected_steps]

        user_answers = state["answers"]
        results = []

        for i in range(expected_steps):
            result = "✅" if user_answers[i] == correct[i] else f"❌ ({correct[i]})"
            results.append(f"{i + 1}) {user_answers[i]} {result}")
        
        await message.answer("Result:\n" + "\n".join(results))

        await self.start_game(message, level)

    async def send_correct_answer(self, message: Message, state: dict):
        verb = state["verb"]
        await message.answer(
            f"Correct forms:\n"
            f"Infinitive: <b>{verb['infinitive']}</b>\n"
            f"past_simple_v2: <b>{verb['past_simple_v2']}</b>\n"
            f"past_participle_v3: <b>{verb['past_participle_v3']}</b>\n"
        )

    #     form_map = {
    #         "Easy": "infinitive",
    #         "Medium": "past_simple_v2",
    #         "Hard": "past_participle_v3"
    #     }

    #     form_field = form_map.get(level, "infinitive")
    #     correct_answer = verb[form_field].lower()

    #     # Запоминаем состояние игры
    #     self.user_states[user_id] = {
    #         "in_game": True,
    #         "correct_answer": correct_answer,
    #         "verb": verb,
    #         "level": level
    #     }

    #     await message.answer(
    #         f"How translate (infinitive): <b>{verb['translate']}</b>?",
    #         reply_markup=self.session_keyboard
    #     )

    # async def check_answer(self, message: Message):
    #     user_id = message.from_user.id
    #     state = self.user_states.get(user_id)

    #     if not state or not state.get("in_game"):
    #         await message.answer("Start a new game. Choose level!")
    #         return
        
    #     user_answer = message.text.strip().lower()

    #     if user_answer == "go back":
    #         self.user_states[user_id]["in_game"] = False
    #         await message.answer(
    #             "You've left the game. Choose level again",
    #             reply_markup=games_irregular_verbs_choose_level
    #         )
    #         return
        
    #     if user_answer == "don't know":
    #         await message.answer(
    #             f"Correct answer was: <b>{state['correct_answer']}</b>"
    #         )
    #         await self.start_game(message, state["level"])
    #         return
        
    #     if user_answer == state["correct_answer"]:
    #         await message.answer("✅ Yes, correct!")
    #     else:
    #         await message.answer(
    #             f"❌ Wrong! Correct answer was: <b>{state['correct_answer']}</b>"
    #         )

    #     await self.start_game(message, state["level"])



# class IrregularVerbsGame:
#     def __init__(self, db):
#         self.db = db
#         self.user_states = {} # user_id: {"correct_answer": "go", "verb": {...}}

#     async def start_game(self, message: Message, level: str):
#         user_id = message.from_user.id
#         verb = self.db.get_random_verb()

#         if not verb:
#             await message.answer("Connection to DB is lost. Try again later")
#             return
        
#         self.user_states[user_id] = {
#             "correct_answer": verb["infinitive"].lower(),
#             "verb": verb,
#             "level": level
#         }

#         await message.answer(
#             f"How translate (infinitive): <b>{verb['translate']}</b>?",
#             reply_markup=games_irregular_verbs_choose_level
#         )

#     async def check_answer(self, message: Message):
#         user_id = message.from_user.id
#         state = self.user_states.get(user_id)

#         if not state:
#             await message.answer("Try to start game, choose level")
#             return

#         user_answer = message.text.strip().lower()
#         correct_answer = state["correct_answer"]

#         if user_answer == correct_answer:
#             await message.answer("✅ Yes, correct!")
#         else:
#             await message.answer(f"❌ Wrong! Correct answer: <b>{correct_answer}</b>")

#         await self.start_game(message, state["level"])