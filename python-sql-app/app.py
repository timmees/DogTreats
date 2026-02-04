from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

# Zentrale Flask-Anwendung: definiert die Web-Routen, verbindet Templates mit Logik
# und koordiniert Datenbankzugriffe sowie Abo-, Warenkorb- und Nutzerfunktionen.

#Importe von Funktionen aus anderen Dateien
from dogtreats.db import get_db_connection as _get_db_connection
from dogtreats.services.plans_service import recommend_plans
from dogtreats.services.cart_service import (
    cart_get,
    cart_add_item,
    cart_remove_item,
    cart_clear,
    cart_get_item,
    cart_set_item
)
from dogtreats.services.subs_service import (
    subs_list,
    subs_create_from_cart,
    subs_pause,
    subs_resume,
    subs_cancel
)

app = Flask(__name__)
app.secret_key = "secretkey" #für Sessions, aus Flask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "dogtreats.db")


def get_db_connection():
    return _get_db_connection(DB_PATH)

#Ab hier: Routes auf templates + Backend Logik
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
            return render_template("profile.html", message=message, username=username_in_session)

        conn = get_db_connection()
        cur = conn.cursor() #cursor liest DB-Abfragen

        #User registrieren sofern dieser noch nicht existiert
        if action == "register":
            cur.execute("SELECT username FROM users WHERE username = ?", (username,))
            existing = cur.fetchone()
            if existing:
                message = "Benutzername ist bereits vergeben."
            else:
                cur.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, password)
                )
                conn.commit()
                session["username"] = username
                conn.close()
                return redirect(url_for("index"))

        elif action == "login":
            
            # Login: Passwort mit Datenbankeintrag vergleichen
            cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            row = cur.fetchone()
            if row and row["password_hash"] == password:
                session["username"] = username
                conn.close()
                return redirect(url_for("index"))
            else:
                message = "Benutzername oder Passwort ist falsch."

        conn.close()

    return render_template("profile.html", message=message, username=username_in_session)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/create_dog", methods=["GET", "POST"])
def create_dog():
    if request.method == "POST":
        if "username" not in session:
            return redirect(url_for("profile"))

        #Benutzer aus Session lesen
        username = session["username"]

        #Eingabedaten aus Formular zum Anlegen eines Hundes
        dog_name = request.form.get("name") # durch get kein Fehler wenn NULL
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

        return redirect(url_for("create_dog")) #Nach dem Anlegen des Hundes zurück zum Formular 

    return render_template("create_dog.html") # rendert das Formular und schickt es an den Browser


@app.route("/plans/all", methods=["GET", "POST"])
def plans_all():
    if "username" not in session:
        return render_template("plans_all.html", logged_in=False)

    username = session["username"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, breed, age_years, weight_kg, sensitivities FROM dogs WHERE username = ? ORDER BY id DESC",
        (username,)
    )
    #holt alle passenden Hunde eines Users (letzte SQL Select)
    dogs = cur.fetchall()

    selected_dog_id = None
    selected_dog = None
    plans = [] #leere Liste, später kommen 3 empfohlende Abos rein

    if request.method == "POST":
        selected_dog_id = request.form.get("dog_id")

        cur.execute(
            "SELECT id, name, breed, age_years, weight_kg, sensitivities FROM dogs WHERE username = ? AND id = ?",
            (username, selected_dog_id)
        )
        selected_dog = cur.fetchone() #=letzter SQL-Select

        if selected_dog:
            plans = recommend_plans(cur, selected_dog)

    conn.close()

    #Variablen ans Template übergeben
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
    subscriptions = subs_list(cur, username)
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
    items = cart_get(session)
    return render_template("cart.html", items=items)


@app.route("/cart/add", methods=["POST"])
def cart_add():
    if "username" not in session:
        return redirect(url_for("profile"))

    dog_id = request.form.get("dog_id")
    dog_name = request.form.get("dog_name")
    plan_title = request.form.get("plan_title")
    product_name = request.form.get("product_name")
    base_amount_g = float(request.form.get("base_amount_g")) #float wegen 3,5 Tagen
    base_price_eur = float(request.form.get("base_price_eur"))
    grams_per_day = float(request.form.get("grams_per_day"))
    size_days = float(request.form.get("size_days"))

    amount_g = round(grams_per_day * size_days) #Gesamtmenge in Gramm
    price = (base_price_eur / base_amount_g) * amount_g #Preis berechnen
    price = round(price, 2) #auf 2 Nachkommastellen runden

    item = {
        "dog_id": dog_id,
        "dog_name": dog_name,
        "plan_title": plan_title,
        "product_name": product_name,
        "days": size_days,
        "amount_g": amount_g,
        "price": price
    }

    cart_add_item(session, item) #Item zum Warenkorb hinzufügen
    return redirect(url_for("cart")) 


@app.route("/cart/remove/<int:item_index>", methods=["POST"])
def cart_remove(item_index):
    cart_remove_item(session, item_index)
    return redirect(url_for("cart"))


@app.route("/delivery_interval/<int:item_index>", methods=["GET", "POST"])
def delivery_interval(item_index):
    item = cart_get_item(session, item_index)
    if item is None:
        return redirect(url_for("cart"))

    rec = item.get("days", 7) #nutze Wert von days, wenn dieser nicht existiert -> Default = 7
    try:
        rec = float(rec) #sicherstellen, dass rec ein float ist für 3,5 und Strings
    except:
        rec = 7.0

    rec_days_int = 4 if rec == 3.5 else int(rec)

    #Intervall kann auf die 2-oder 4-fache Länge eingestellt werden
    options = [
        rec_days_int,
        rec_days_int * 2,
        rec_days_int * 4
    ]

    if request.method == "POST":
        chosen_int = int(request.form.get("interval_days")) #Interval Days werden zu int

        if chosen_int not in options:
            return redirect(url_for("cart"))

        item["delivery_interval_days"] = chosen_int
        cart_set_item(session, item_index, item)
        return redirect(url_for("cart"))

    #Variablen ans Template übergeben
    return render_template(
        "delivery_interval.html",
        item=item, 
        item_index=item_index,
        rec_days=rec_days_int,
        options=options,
        message=None
    )


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "username" not in session:
        return redirect(url_for("profile"))

    items = cart_get(session)
    if not items:
        return redirect(url_for("cart"))

    total = sum(float(it["price"]) for it in items)

    if request.method == "POST":
        username = session["username"]
        conn = get_db_connection()
        cur = conn.cursor()
        subs_create_from_cart(cur, username, items)
        conn.commit()
        conn.close()
        cart_clear(session)
        flash("Abo erfolgreich abgeschlossen", "success")
        return redirect(url_for("index"))

    return render_template("checkout.html", items=items, total=total)




@app.route("/subscriptions/<int:sub_id>/pause", methods=["POST"])
def pause_subscription(sub_id):
    if "username" not in session:
        return redirect(url_for("profile"))

    username = session["username"]
    pause_days = int(request.form.get("pause_days", 14))

    conn = get_db_connection()
    cur = conn.cursor()
    subs_pause(cur, username, sub_id, pause_days)
    conn.commit()
    conn.close()

    return redirect(url_for("manage_subscriptions"))



@app.route("/subscriptions/<int:sub_id>/resume")
def resume_subscription(sub_id):
    if "username" not in session:
        return redirect(url_for("profile"))

    username = session["username"]

    conn = get_db_connection()
    cur = conn.cursor()
    subs_resume(cur, username, sub_id)
    conn.commit()
    conn.close()

    return redirect(url_for("manage_subscriptions"))


@app.route("/subscriptions/<int:sub_id>/cancel", methods=["POST"])
def cancel_subscription(sub_id):
    if "username" not in session:
        return redirect(url_for("profile"))

    username = session["username"]

    conn = get_db_connection()
    cur = conn.cursor()
    subs_cancel(cur, username, sub_id)
    conn.commit()
    conn.close()

    return redirect(url_for("manage_subscriptions"))


if __name__ == "__main__": #app kann gestartet werden
    app.run(debug=True) #zeigt Fehlermeldungen im Browser
