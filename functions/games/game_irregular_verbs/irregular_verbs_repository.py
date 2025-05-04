import psycopg2
import random
import os

from config import POSTGRES_URL

class IrregularVerbsRepository:
    def __init__(self):
        self.conn = psycopg2.connect(POSTGRES_URL)
        self.conn.autocommit = True

    def get_random_verb(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, infinitive, past_simple_v2, past_participle_v3, translate_word
                FROM bfa_games.irregular_verbs
                ORDER BY RANDOM()
                LIMIT 1
            """)
            row = cursor.fetchone()

        if row:
            return {
                "id": row[0],
                "infinitive": row[1],
                "past_simple_v2": row[2],
                "past_participle_v3": row[3],
                "translate": row[4]
            }
        return None

    def close(self):
        self.conn.close()