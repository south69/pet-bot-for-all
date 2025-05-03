import sqlite3
import random
import os
from datetime import datetime



class HabitsRepository:
    def __init__(self, db_path=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = db_path or os.path.join(base_dir, "habits.db")

    def _connect(self):
        # print(f"[DEBUG] Using DB at: {self.db_path}")
        return sqlite3.connect(self.db_path)
    
    def add_habit(self, 
                  username: str,
                  habit_name: str,
                  time_notification: str,
                  status_habit: str
                  ):
        conn = self._connect()
        cursor = conn.cursor()

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            """
            INSERT INTO habits_task (
            habit_name, time_notification, last_notification, 
            status_habit, username, 
            created_at, updated_at, deleted_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                habit_name,
                time_notification,
                None,
                status_habit,
                username,
                created_at,
                None,
                None
            )
        )

        conn.commit()
        conn.close()