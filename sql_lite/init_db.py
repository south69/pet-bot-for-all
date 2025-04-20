import sqlite3
import pandas as pd
import os

def create_irregular_verbs_table():
    # Определяем путь к текущей директории, где лежит этот файл
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "irregular_verbs.db")
    csv_path = os.path.join(base_dir, "irregular_verbs.csv")

    # Подключение к базе
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создание таблицы, если её нет
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS irregular_verbs (
            id INTEGER NOT NULL,
            infinitive TEXT NOT NULL,
            past_simple_v2 TEXT NOT NULL,
            past_participle_v3 TEXT NOT NULL,
            translate TEXT NOT NULL
        );
        '''
    )

    # Загрузка данных из CSV
    df = pd.read_csv(csv_path)
    df.columns = ['id', 'infinitive', 'past_simple_v2', 'past_participle_v3', 'translate']

    # Перезапись таблицы
    df.to_sql('irregular_verbs', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print('Database initialized with irregular verbs')


# Если запускать этот файл отдельно — инициализируем базу
if __name__ == "__main__":
    create_irregular_verbs_table()
