-- NICHT mehr nötig für Betrieb der Applikation, da Daten schon in DB sind! Nur für Doku relevant
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    origin TEXT,
    quality_notes TEXT,

    base_amount_g INTEGER NOT NULL,  
    base_price_eur REAL NOT NULL,    
    image_url TEXT,

    FOREIGN KEY (category_id) REFERENCES categories(id)
);
