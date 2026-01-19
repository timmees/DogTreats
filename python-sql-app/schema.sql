PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    name TEXT NOT NULL,
    breed TEXT NOT NULL,
    age_years INTEGER,
    weight_kg REAL,
    sensitivities TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
);

CREATE TABLE subscriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    dog_name TEXT,
    plan_title TEXT,
    interval_days INTEGER,
    price REAL,
    is_paused INTEGER DEFAULT 0,
    pause_until DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
