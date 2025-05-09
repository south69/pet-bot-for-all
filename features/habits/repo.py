import psycopg2
import random
import os
from datetime import datetime

from config.config import POSTGRES_URL


class HabitsRepository:
    def __init__(self):
        self.conn = psycopg2.connect(POSTGRES_URL)
        self.conn.autocommit = True
    
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
                    None
                )
            )

    def close(self):
        self.conn.close()
