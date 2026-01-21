#Logik für Abo-Empfehlungen
def estimate_grams_per_day(weight_kg):
    try:
        w = float(weight_kg)
    except:
        w = None
    return max(50, int(w * 20)) if w else 200 #20 Gramm pro Tag pro Kg, sonst 200g/Tag


def get_product(cur, category_name, exclude_keyword=None):
    if exclude_keyword:
        cur.execute("""
            SELECT p.name, p.description, p.base_amount_g, p.base_price_eur, p.image_url,
                   c.name AS category_name
            FROM products p
            JOIN categories c ON p.category_id = c.id
            WHERE c.name = ?
              AND LOWER(p.name) NOT LIKE ?
            ORDER BY p.id ASC
            LIMIT 1
        """, (category_name, f"%{exclude_keyword.lower()}%"))
    else:
        cur.execute("""
            SELECT p.name, p.description, p.base_amount_g, p.base_price_eur, p.image_url,
                   c.name AS category_name
            FROM products p
            JOIN categories c ON p.category_id = c.id
            WHERE c.name = ?
            ORDER BY p.id ASC
            LIMIT 1
        """, (category_name,))
    return cur.fetchone()

#baut ein Abo-Objekt aus Produkt, Bild und Text, anzeigbar im Frontend
def build_plan(plan_id, title, product, note, tags, grams_per_day):
    if not product:
        return None
    return {
        "plan_id": plan_id,
        "title": title,
        "note": note,
        "tags": tags,
        "product_name": product["name"],
        "product_desc": product["description"],
        "category_name": product["category_name"],
        "base_amount_g": int(product["base_amount_g"]),
        "base_price_eur": float(product["base_price_eur"]),
        "image_url": product["image_url"],
        "grams_per_day": grams_per_day
    }


def recommend_plans(cur, dog):
    age = dog["age_years"]
    sens = (dog["sensitivities"] or "").lower()

    is_puppy = age is not None and age <= 1
    is_senior = age is not None and age >= 8

    grams_per_day = estimate_grams_per_day(dog["weight_kg"])

    catalog = []

    catalog.append(build_plan(
        "base",
        "Basis-Abo",
        get_product(cur, "Trockenfutter"),
        f"Solide Grundversorgung für {dog['name']}.",
        ["base"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "grainfree",
        "Getreidefrei-Abo",
        get_product(cur, "Getreidefrei"),
        "Ohne Getreide – gut verträglich für sensible Hunde.",
        ["getreide"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "sensitive",
        "Sensitiv-Magen-Abo",
        get_product(cur, "Sensitiv"),
        "Besonders schonend für empfindlichen Magen.",
        ["magen", "sensitiv"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "senior",
        "Senior-Abo",
        get_product(cur, "Sensitiv"),
        "Leicht verdaulich und angepasst an ältere Hunde.",
        ["senior"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "junior",
        "Junior-/Welpen-Abo",
        get_product(cur, "Trockenfutter"),
        "Für Wachstum und hohen Energiebedarf.",
        ["junior"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "rindfrei",
        "Rindfrei-Abo",
        get_product(cur, "Trockenfutter", "rind"),
        "Ohne Rind – bei entsprechender Unverträglichkeit.",
        ["rind"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "huhnfrei",
        "Huhnfrei-Abo",
        get_product(cur, "Trockenfutter", "huhn"),
        "Ohne Huhn – geeignet bei Allergien.",
        ["huhn"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "fischfrei",
        "Fischfrei-Abo",
        get_product(cur, "Trockenfutter", "fisch"),
        "Ohne Fisch – für empfindliche Hunde.",
        ["fisch"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "low_energy",
        "Low-Energy-Abo",
        get_product(cur, "Trockenfutter"),
        "Reduzierte Energiezufuhr für ruhige Hunde.",
        ["low_energy"],
        grams_per_day
    ))

    catalog.append(build_plan(
        "chew",
        "Kauartikel-Abo",
        get_product(cur, "Kauartikel"),
        "Kauartikel zur Beschäftigung – Ergänzung zum Futter.",
        ["chew"],
        grams_per_day
    ))

    catalog = [c for c in catalog if c]

    #Auswahl basierend auf Score s
    #Berechnet für jedes Modell einen Score ->Die 3 Abos mit dem höchsten Score werden empfohlen
    def score(p):
        s = 0
        if "getreideunverträglichkeit" in sens and "getreide" in p["tags"]:
            s += 50
        if "empfindlicher magen" in sens and "magen" in p["tags"]:
            s += 45
        if "rind-unverträglichkeit" in sens and "rind" in p["tags"]:
            s += 60 #60= sehr wichtig
        if "huhn-unverträglichkeit" in sens and "huhn" in p["tags"]:
            s += 60
        if "fisch-unverträglichkeit" in sens and "fisch" in p["tags"]:
            s += 60
        if "niedriger energiebedarf" in sens and "low_energy" in p["tags"]:
            s += 40
        if is_senior and "senior" in p["tags"]:
            s += 40
        if is_puppy and "junior" in p["tags"]:
            s += 40
        if "base" in p["tags"]:
            s += 10 #Basis->kein wirklicher Vorteil für dieses Abo
        return s

    catalog.sort(key=score, reverse=True) #sortiere nach Score absteigend

    return catalog[:3] #Gib die 3 besten Abos zurück

#Beispiel: Welpe mit Rind-Unverträglichkeit ausgewählt -> Abo für Welpen bekommt +40; Abo für Rind-Unverträglichkeit bekommt+60