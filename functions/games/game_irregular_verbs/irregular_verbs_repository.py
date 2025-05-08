import psycopg2
import random
import os
import matplotlib.pyplot as plt
from io import BytesIO
from aiogram.types import BufferedInputFile

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
    
    def create_log_irregular_verb(self, *, user_id, username, game_id, game_name,
                                  level_game, word_given, word_answered, correct_flg):
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO bfa_games.games_log (
                    user_id, username, game_id, game_name,
                    level_game, word_given, word_answered, 
                    correct_flg
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    user_id, username, game_id, game_name,
                    level_game, word_given, word_answered, 
                    correct_flg
                )
            )

    def get_user_statistics(self, user_id: int, period: str = "all"):
        date_filter = ""
        if period == "today":
            date_filter = "AND played_at::date = CURRENT_DATE"
        elif period == "week":
            date_filter = "AND played_at >= NOW() - INTERVAL '7 days'"
        elif period == "month":
            date_filter = "AND played_at >= NOW() - INTERVAL '1 month'"
        
        with self.conn.cursor() as cursor:
            cursor.execute(f"""
                    SELECT 
                        COUNT(*) AS total_games,
                        COUNT(*) FILTER (WHERE correct_flg) AS correct_answers,
                        level_game
                        FROM bfa_games.games_log
                        WHERE user_id = %s AND game_name = 'Irregular Verbs'
                        {date_filter}
                        GROUP BY level_game
                    """, (user_id,))
            rows = cursor.fetchall()

        stats = []
        for row in rows:
            total, correct, level = row
            percent = round(correct / total * 100) if total > 0 else 0
            stats.append((level, total, correct, percent))
        return stats

    def close(self):
        self.conn.close()

    