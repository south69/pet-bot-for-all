-- Все таблицы внутри папки bfa_games: 
-- bfa_games (schema)
    -- games (table)
    -- games_log (table)
    -- irregular_verbs (table)
-- bfa_habits (schema)
    -- habits (table)
    -- habits_log (table)
-- bfa_reminders (schema)
-- bfa_workouts (schema)

-- СОЗДАЮ СХЕМЫ (они же папки): 

CREATE SCHEMA IF NOT EXISTS bfa_games;
CREATE SCHEMA IF NOT EXISTS bfa_habits;
CREATE SCHEMA IF NOT EXISTS bfa_reminders;
CREATE SCHEMA IF NOT EXISTS bfa_workouts;


-- СОЗДАЮ ТАБЛИЦЫ В СХЕМЕ bfa_games:

-- bfa_games.games
CREATE TABLE IF NOT EXISTS bfa_games.games (
    id SERIAL PRIMARY KEY, 
    name TEXT NOT NULL
);

-- bfa_games.games_log
CREATE TABLE IF NOT EXISTS bfa_games.games_log (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    username TEXT,
    game_id INTEGER NOT NULL,
    game_name TEXT,
    level_game TEXT,
    word_given TEXT,
    word_answered TEXT,
    correct_flg BOOLEAN,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- bfa_games.irregular_verbs
CREATE TABLE IF NOT EXISTS bfa_games.irregular_verbs (
    id SERIAL PRIMARY KEY,
    infinitive TEXT NOT NULL,
    past_simple_v2 TEXT NOT NULL,
    past_participle_v3 TEXT NOT NULL,
    translate_word TEXT NOT NULL
);



-- СОЗДАЮ ТАБЛИЦЫ В СХЕМЕ bfa_habits:

-- bfa_habits.habits
CREATE TABLE IF NOT EXISTS bfa_habits.habits (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    time_notification TIME NOT NULL,
    last_notification TIMESTAMP,
    status TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    username TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- bfa_habits.habits_log
CREATE TABLE IF NOT EXISTS bfa_habits.habits_log (
    id SERIAL PRIMARY KEY,
    habit_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    username TEXT,
    action_type TEXT,
    note TEXT,
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);