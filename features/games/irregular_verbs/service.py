from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

import psycopg2
import os
import logging

from config import POSTGRES_URL
from features.games.irregular_verbs.keyboards import games_irregular_verbs_menu, games_irregular_verbs_choose_level
from features.games.irregular_verbs.repo import IrregularVerbsRepository

GAME_ID = 1
GAME_NAME = "Irregular Verbs"

class IrregularVerbsGame:
    def __init__(self, db: IrregularVerbsRepository):
        self.db = db
        self.user_states = {}

        self.session_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="leave the game"), KeyboardButton(text="Don't know")]
            ],
            resize_keyboard=True
        )

    async def start_game(self, message: Message, level: str):
        logging.debug(f"[start_game] Пользователь: {message.from_user.username}, уровень: {level}")
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
        logging.debug(f"[check_answer] Ответ от пользователя {message.from_user.username}: {message.text}")
        user_id = message.from_user.id
        state = self.user_states.get(user_id)

        if not state or not state.get("in_game"):
            await message.answer("Start a new game by choose a level again")
            return
        
        user_input  = message.text.strip().lower()

        if user_input  == "leave the game":
            state["in_game"] = False
            await message.answer(
                "You've left the game. Please choose a level again",
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
        
        await message.answer("Your result:\n" + "\n".join(results))

        # Логирование результатов игры
        for i in range(expected_steps):
            answer = user_answers[i]
            correct_answer = correct[i]
            is_correct = answer == correct_answer

            self.db.create_log_irregular_verb(
                user_id=message.from_user.id,
                username=message.from_user.username,
                game_id=GAME_ID,
                game_name=GAME_NAME,
                level_game=level,
                word_given=correct_answer,
                word_answered=answer,
                correct_flg=is_correct
            )


        await self.start_game(message, level)

    async def send_correct_answer(self, message: Message, state: dict):
        verb = state["verb"]
        await message.answer(
            f"The correct forms are:\n"
            f"Infinitive: <b>{verb['infinitive']}</b>\n"
            f"past_simple_v2: <b>{verb['past_simple_v2']}</b>\n"
            f"past_participle_v3: <b>{verb['past_participle_v3']}</b>\n"
        )
