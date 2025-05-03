import sqlite3
import pandas as pd
import os

def create_habits_tables():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "habits.db")

    if os.path.exists(db_path):
        # os.remove(db_path)
        # print('Old habits.db removed')
        print("DB already creted")

    # Пути к файлам CSV
    habits_task_csv = os.path.join(base_dir, "habits_task.csv")
    habits_log_csv = os.path.join(base_dir, "habits_log.csv")

    # Подключение к БД
    conn = sqlite3.connect(db_path)

    # habits_task
    df_tasks = pd.read_csv(habits_task_csv)
    df_tasks.to_sql('habits_task', conn, if_exists='replace', index=False)

    # habits_log
    df_log = pd.read_csv(habits_log_csv)
    df_log.to_sql('habits_log', conn, if_exists='replace', index=False)

    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(habits_task);")
    columns = cursor.fetchall()
    print("=== Columns in habits_task ===")
    for col in columns:
        print(col)

    print('DB initialized with habits tables')

if __name__ == "__main__":
    create_habits_tables()