import sqlite3
import random
import os
from datetime import datetime



class HabitsRepository:
    def __init__(self, db_path=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = db_path or os.path.join(base_dir, "habits.db")

    def _connect(self):
        return sqlite3.connect(self.db_path)