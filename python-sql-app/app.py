from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os   

app = Flask(__name__)
app.secret_key = "secretkey"  


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "dogtreats.db")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    message = None
    username_in_session = session.get("username")

    if request.method == "POST":
        action = request.form.get("action")  
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            message = "Bitte Benutzername und Passwort eingeben."
            return render_template(
                "profile.html",
                message=message,
                username=username_in_session
            )

        conn = get_db_connection()
        cur = conn.cursor()

        if action == "register":
            # Prüfen, ob der Benutzername schon existiert
            cur.execute("SELECT username FROM users WHERE username = ?", (username,))
            existing = cur.fetchone()
            if existing:
                message = "Benutzername ist bereits vergeben."
            else:
                # Passwort speichern
                cur.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, password)
                )
                conn.commit()
                session["username"] = username
                conn.close()
                return redirect(url_for("index"))

        elif action == "login":
            cur.execute(
                "SELECT password_hash FROM users WHERE username = ?",
                (username,)
            )
            row = cur.fetchone()
            if row and row["password_hash"] == password:
                session["username"] = username
                conn.close()
                return redirect(url_for("index"))
            else:
                message = "Benutzername oder Passwort ist falsch."
        conn.close()

    return render_template(
        "profile.html",
        message=message,
        username=username_in_session
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/create_dog", methods=["GET", "POST"])
def create_dog():
    if request.method == "POST":
        if "username" not in session:
            return redirect(url_for("profile"))

        username = session["username"]

        dog_name = request.form.get("name")
        breed = request.form.get("breed")
        age_years = request.form.get("age_years")
        weight_kg = request.form.get("weight_kg")
        sensitivities = request.form.get("sensitivities")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO dogs (username, name, breed, age_years, weight_kg, sensitivities)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (username, dog_name, breed, age_years, weight_kg, sensitivities)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("create_dog"))

    return render_template("create_dog.html")



@app.route("/plans/all", methods=["GET", "POST"])
def plans_all():
    # 1) Nicht eingeloggt
    if "username" not in session:
        return render_template("plans_all.html", logged_in=False)

    username = session["username"]

    # Hunde des Users laden
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, breed, age_years, weight_kg, sensitivities FROM dogs WHERE username = ? ORDER BY id DESC", (username,))
    dogs = cur.fetchall()

    selected_dog_id = None
    selected_dog = None
    plans = []

    if request.method == "POST":
        selected_dog_id = request.form.get("dog_id")

        # Hund laden
        cur.execute(
            "SELECT id, name, breed, age_years, weight_kg, sensitivities FROM dogs WHERE username = ? AND id = ?",
            (username, selected_dog_id)
        )
        selected_dog = cur.fetchone()

        if selected_dog:
            # einfache „Verbrauchs“-Schätzung: 20g pro kg Körpergewicht pro Tag
            # Falls Gewicht fehlt -> Default 200g/Tag
            try:
                w = float(selected_dog["weight_kg"]) if selected_dog["weight_kg"] is not None and str(selected_dog["weight_kg"]).strip() != "" else None
            except:
                w = None
            grams_per_day = max(50, int(w * 20)) if w else 200

            sensitivities = (selected_dog["sensitivities"] or "").lower()
            wants_grainfree = "getreide" in sensitivities or "sensitiv" in sensitivities

            # Produkte passend ziehen (jeweils 1 Produkt pro Modell, erstmal simpel)
            def get_product_by_category(cat_name: str):
                cur.execute("""
                    SELECT p.id, p.name, p.description, p.base_amount_g, p.base_price_eur, p.image_url,
                           c.name AS category_name
                    FROM products p
                    JOIN categories c ON p.category_id = c.id
                    WHERE c.name = ?
                    ORDER BY p.id ASC
                    LIMIT 1;
                """, (cat_name,))
                return cur.fetchone()

            # Modell 1: „Basis“ -> Trockenfutter (oder Sensitiv, wenn Allergie/Sensitiv)
            prod1 = get_product_by_category("Sensitiv") if wants_grainfree else get_product_by_category("Trockenfutter")

            # Modell 2: Getreidefrei
            prod2 = get_product_by_category("Getreidefrei")

            # Modell 3: Kauartikel (Snack-Paket)
            prod3 = get_product_by_category("Kauartikel")

            def build_plan(plan_id, title, product_row, note):
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

            plans = [
                build_plan(
                    "base",
                    "Basis-Abo (angepasst)",
                    prod1,
                    f"Für {selected_dog['name']} ({selected_dog['breed']}). Empfehlung basiert auf Rasse/Grundbedarf und deinen Angaben."
                ),
                build_plan(
                    "grainfree",
                    "Getreidefrei-Abo",
                    prod2,
                    "Für sensible Hunde oder wenn du bewusst getreidefrei füttern möchtest."
                ),
                build_plan(
                    "chew",
                    "Kauartikel-Abo",
                    prod3,
                    "Für Beschäftigung und Kaubedürfnis – ideal als Ergänzung."
                ),
            ]
            plans = [p for p in plans if p is not None]

    conn.close()

    return render_template(
        "plans_all.html",
        logged_in=True,
        dogs=dogs,
        selected_dog_id=selected_dog_id,
        selected_dog=selected_dog,
        plans=plans
    )


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/manage_subscriptions")
def manage_subscriptions():
    if "username" not in session:
        return redirect(url_for("profile"))

    username = session["username"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, dog_name, plan_title, interval_days, price, is_paused, pause_until
        FROM subscriptions
        WHERE username = ?
        ORDER BY created_at DESC
    """, (username,))
    subscriptions = cur.fetchall()
    conn.close()

    return render_template("manage_subscriptions.html", subscriptions=subscriptions)



@app.route("/mydogs")
def mydogs():
    if "username" not in session:
        return redirect(url_for("profile"))

    username = session["username"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, breed, age_years, weight_kg, sensitivities FROM dogs WHERE username = ? ORDER BY id DESC",
        (username,)
    )
    dogs = cur.fetchall()
    conn.close()

    return render_template("mydogs.html", dogs=dogs)



@app.route("/track_orders")
def track_orders():
    if "username" not in session:
        return redirect(url_for("profile"))
    return render_template("track_orders.html")


@app.route("/order_history")
def order_history():
    if "username" not in session:
        return redirect(url_for("profile"))
    return render_template("order_history.html")

@app.route("/all_products")
def all_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.id, p.name, p.description, p.origin, p.quality_notes,
               p.base_amount_g, p.base_price_eur,
               c.name AS category_name
        FROM products p
        JOIN categories c ON p.category_id = c.id
        ORDER BY c.name, p.name;
    """)
    products = cur.fetchall()
    conn.close()

    return render_template("all_products.html", products=products)

@app.route("/cart")
def cart():
    items = session.get("cart", [])
    return render_template("cart.html", items=items)


@app.route("/checkout")
def checkout():
    items = session.get("cart_items", [])
    user_id = session["user_id"]

    for it in items:
        db.execute("""
            INSERT INTO subscriptions
            (user_id, dog_name, plan_title, interval_days, price)
            VALUES (?, ?, ?, ?, ?)
        """, (
            user_id,
            it["dog_name"],
            it["plan_title"],
            it["days"],
            it["price"]
        ))

    session.pop("cart_items", None)
    return redirect("/account")


@app.route("/cart/remove/<int:item_index>", methods=["POST"])
def cart_remove(item_index):
    items = session.get("cart", [])
    if 0 <= item_index < len(items):
        items.pop(item_index)
        session["cart"] = items
    return redirect(url_for("cart"))

@app.route("/delivery_interval/<int:item_index>", methods=["GET", "POST"])
def delivery_interval(item_index):
    items = session.get("cart", [])
    if not (0 <= item_index < len(items)):
        return redirect(url_for("cart"))

    item = items[item_index]

    rec = item.get("days", 7)
    try:
        rec = float(rec)
    except:
        rec = 7.0

    rec_days_int = 4 if rec == 3.5 else int(rec)

    options = [
        rec_days_int,
        rec_days_int * 2,
        rec_days_int * 4
    ]

    if request.method == "POST":
        chosen = request.form.get("interval_days", "").strip()
        try:
            chosen_int = int(chosen)
        except:
            chosen_int = None

        if chosen_int not in options:
            return render_template(
                "delivery_interval.html",
                item=item,
                item_index=item_index,
                rec_days=rec_days_int,
                options=options,
                message="Bitte eine der angebotenen Optionen auswählen."
            )

        item["delivery_interval_days"] = chosen_int
        items[item_index] = item
        session["cart"] = items

        return redirect(url_for("cart"))

    return render_template(
        "delivery_interval.html",
        item=item,
        item_index=item_index,
        rec_days=rec_days_int,
        options=options,
        message=None
    )



@app.route("/cart/add", methods=["POST"])
def cart_add():
    if "username" not in session:
        return redirect(url_for("profile"))

    # Daten aus dem Formular
    dog_id = request.form.get("dog_id")
    dog_name = request.form.get("dog_name")
    plan_title = request.form.get("plan_title")
    product_name = request.form.get("product_name")
    base_amount_g = float(request.form.get("base_amount_g"))
    base_price_eur = float(request.form.get("base_price_eur"))
    grams_per_day = float(request.form.get("grams_per_day"))

    
    size_days = float(request.form.get("size_days"))  

    amount_g = round(grams_per_day * size_days)
    price = (base_price_eur / base_amount_g) * amount_g
    price = round(price, 2)

    item = {
        "dog_id": dog_id,
        "dog_name": dog_name,
        "plan_title": plan_title,
        "product_name": product_name,
        "days": size_days,
        "amount_g": amount_g,
        "price": price
    }

    cart_items = session.get("cart", [])
    cart_items.append(item)
    session["cart"] = cart_items

    return redirect(url_for("cart"))




if __name__ == "__main__":
    app.run(debug=True)
