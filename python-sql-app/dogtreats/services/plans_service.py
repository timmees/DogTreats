def estimate_grams_per_day(weight_kg):
    try:
        w = float(weight_kg) if weight_kg is not None and str(weight_kg).strip() != "" else None
    except:
        w = None
    return max(50, int(w * 20)) if w else 200

def get_product_by_category(cur, category_name):
    cur.execute("""
        SELECT p.id, p.name, p.description, p.base_amount_g, p.base_price_eur, p.image_url,
               c.name AS category_name
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE c.name = ?
        ORDER BY p.id ASC
        LIMIT 1
    """, (category_name,))
    return cur.fetchone()

def build_plan(plan_id, title, product_row, note, grams_per_day):
    if not product_row:
        return None
    return {
        "plan_id": plan_id,
        "title": title,
        "note": note,
        "product_name": product_row["name"],
        "product_desc": product_row["description"],
        "category_name": product_row["category_name"],
        "base_amount_g": int(product_row["base_amount_g"]),
        "base_price_eur": float(product_row["base_price_eur"]),
        "image_url": product_row["image_url"],
        "grams_per_day": grams_per_day,
    }

def recommend_plans(cur, dog_row):
    grams_per_day = estimate_grams_per_day(dog_row["weight_kg"])
    sensitivities = (dog_row["sensitivities"] or "").lower()
    wants_grainfree = "getreide" in sensitivities or "sensitiv" in sensitivities

    prod1 = get_product_by_category(cur, "Sensitiv") if wants_grainfree else get_product_by_category(cur, "Trockenfutter")
    prod2 = get_product_by_category(cur, "Getreidefrei")
    prod3 = get_product_by_category(cur, "Kauartikel")

    plans = [
        build_plan(
            "base",
            "Basis-Abo (angepasst)",
            prod1,
            f"Für {dog_row['name']} ({dog_row['breed']}). Empfehlung basiert auf Rasse/Grundbedarf und deinen Angaben.",
            grams_per_day
        ),
        build_plan(
            "grainfree",
            "Getreidefrei-Abo",
            prod2,
            "Für sensible Hunde oder wenn du bewusst getreidefrei füttern möchtest.",
            grams_per_day
        ),
        build_plan(
            "chew",
            "Kauartikel-Abo",
            prod3,
            "Für Beschäftigung und Kaubedürfnis – ideal als Ergänzung.",
            grams_per_day
        ),
    ]
    return [p for p in plans if p is not None]
