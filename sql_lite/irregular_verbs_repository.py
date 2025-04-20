import sqlite3
import random
import os



class IrregularVerbsRepository:
    def __init__(self, db_path=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = db_path or os.path.join(base_dir, "irregular_verbs.db")

    def get_random_verb(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * from irregular_verbs order by random() limit 1;")
        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                # "id": result [0],
                "infinitive": result[1],
                "past_simple_v2": result[2],
                "past_participle_v3": result[3],
                "translate": result[4]
            }
        return None


# class IrregularVerbsRepository:
#     def __init__(self, db_path="irregular_verbs.db"):
#         self.db_path = db_path