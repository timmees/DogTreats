PRAGMA foreign_keys = ON;

INSERT OR IGNORE INTO categories (name) VALUES
('Trockenfutter'),
('Trainingssnacks'),
('Kauartikel'),
('Sensitiv'),
('Getreidefrei');

-- Trockenfutter (4)
INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Huhn Trockenfutter', 'Schonend getrocknetes Bio-Huhn, ausgewogene Rezeptur.', 'Deutschland (regional)', 'Bio, ohne künstliche Zusätze', 1000, 10.00, NULL
FROM categories WHERE name='Trockenfutter';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Rind Trockenfutter', 'Proteinreiches Bio-Rind, ideal für aktive Hunde.', 'Deutschland (regional)', 'Bio, transparent', 1000, 11.50, NULL
FROM categories WHERE name='Trockenfutter';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Lamm Trockenfutter', 'Mildes Lamm, gut verträglich.', 'Deutschland/AT (regional)', 'Bio, ohne Zucker', 1000, 12.00, NULL
FROM categories WHERE name='Trockenfutter';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Fisch Trockenfutter', 'Fisch-Protein, ideal für Fell & Haut.', 'EU (nachverfolgbar)', 'Bio, ohne Farbstoffe', 1000, 12.50, NULL
FROM categories WHERE name='Trockenfutter';

-- Trainingssnacks (4)
INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Huhn Minis', 'Kleine Trainingshappen, perfekt fürs Training.', 'Deutschland (regional)', 'Bio, ohne Zusatzstoffe', 200, 4.50, NULL
FROM categories WHERE name='Trainingssnacks';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Rind Minis', 'Kleine Würfel, hohe Akzeptanz.', 'Deutschland (regional)', 'Bio, ohne Aromen', 200, 4.80, NULL
FROM categories WHERE name='Trainingssnacks';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Leberwürfel', 'Sehr beliebt als Belohnung.', 'Deutschland (regional)', 'Bio, single protein', 200, 5.20, NULL
FROM categories WHERE name='Trainingssnacks';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Käsewürfel', 'Für viele Hunde ein Highlight.', 'Deutschland (regional)', 'Bio, ohne Zucker', 200, 4.90, NULL
FROM categories WHERE name='Trainingssnacks';

-- Kauartikel (4)
INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Rinderkopfhaut', 'Kauintensiv, unterstützt Zahnpflege.', 'Deutschland (regional)', 'Ohne Zusätze', 250, 6.50, NULL
FROM categories WHERE name='Kauartikel';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Pansenstreifen', 'Aromatisch, lange Kaudauer.', 'Deutschland (regional)', 'Naturbelassen', 250, 6.20, NULL
FROM categories WHERE name='Kauartikel';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Kaninchenohren', 'Leichter Kauartikel, gut verträglich.', 'Deutschland/EU', 'Natur, ohne Chemie', 150, 5.90, NULL
FROM categories WHERE name='Kauartikel';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Bio-Rindersehnen', 'Zäh und ausdauernd – für starke Kauer.', 'Deutschland (regional)', 'Naturbelassen', 200, 6.80, NULL
FROM categories WHERE name='Kauartikel';

-- Sensitiv (4)
INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Sensitiv: Lamm & Kürbis', 'Milde Rezeptur für empfindliche Hunde.', 'Deutschland', 'Ohne künstliche Zusätze', 1000, 12.00, NULL
FROM categories WHERE name='Sensitiv';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Sensitiv: Pferd Single Protein', 'Single Protein für sensible Hunde.', 'Deutschland/EU', 'Ohne Getreide', 800, 13.50, NULL
FROM categories WHERE name='Sensitiv';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Sensitiv: Insektenprotein', 'Alternative Proteinquelle, gut verträglich.', 'EU (nachverfolgbar)', 'Ohne Farb-/Konservierungsstoffe', 800, 12.90, NULL
FROM categories WHERE name='Sensitiv';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Sensitiv: Fisch & Kartoffel', 'Sanft für Magen und Darm.', 'EU', 'Ohne künstliche Aromen', 1000, 12.70, NULL
FROM categories WHERE name='Sensitiv';

-- Getreidefrei (4)
INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Getreidefrei: Huhn & Süßkartoffel', 'Ohne Getreide, mit Süßkartoffel.', 'Deutschland', 'Ohne Zucker', 1000, 11.80, NULL
FROM categories WHERE name='Getreidefrei';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Getreidefrei: Rind & Erbse', 'Getreidefreie Rezeptur für aktive Hunde.', 'Deutschland', 'Ohne künstliche Zusätze', 1000, 12.20, NULL
FROM categories WHERE name='Getreidefrei';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Getreidefrei: Lachs & Kürbis', 'Omega-3 reich, getreidefrei.', 'EU', 'Ohne Farbstoffe', 1000, 12.90, NULL
FROM categories WHERE name='Getreidefrei';

INSERT INTO products (category_id, name, description, origin, quality_notes, base_amount_g, base_price_eur, image_url)
SELECT id, 'Getreidefrei: Ente & Apfel', 'Milde Ente, getreidefrei.', 'Deutschland/EU', 'Ohne Aromen', 1000, 12.60, NULL
FROM categories WHERE name='Getreidefrei';
