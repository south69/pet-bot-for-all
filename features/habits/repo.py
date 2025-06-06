import psycopg2
import random
import os
import logging

from datetime import datetime

from config import POSTGRES_URL


class HabitsRepository:
    def __init__(self):
        # self.conn = psycopg2.connect(POSTGRES_URL)
        # self.conn.autocommit = True
        try:
            self.conn = psycopg2.connect(POSTGRES_URL)
            self.conn.autocommit = True
            logging.debug("[DB Habits repo] Успешное подключение к базе данных")
        except Exception as e:
            logging.error(f"[DB Habits repo] Ошибка подключения к БД: {e}")
            raise      
    
    def add_habit(self, 
                  username: str,
                  user_id: int,
                  name: str,
                  time_notification: str,
                  status: str
                  ):
        
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO bfa_habits.habits (
                name, time_notification, last_notification, 
                status, user_id, username, 
                created_at, updated_at, deleted_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    name,
                    time_notification,
                    None,
                    status,
                    user_id,
                    username,
                    created_at,
                    None,
                    None,
                )
            )

    def show_habit(self, user_id):

        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    id,
                    name,
                    status,
                    time_notification,
                    last_notification
                FROM bfa_habits.habits
                WHERE status != 'deleted'
                    AND user_id = %s
                """, (user_id,)
            )
            return cursor.fetchall()

    def delete_habit(self, id, user_id):
        
        deleted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE bfa_habits.habits
                SET status = 'deleted',
                    deleted_at = %s
                WHERE id = %s
                    AND user_id = %s
                """,(deleted_at, 
                     id, 
                     user_id,)
            )

    def close(self):
        self.conn.close()
