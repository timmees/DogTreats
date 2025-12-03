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


@app.route("/plans", methods=["GET", "POST"])
def plans():
    if request.method == "POST":
        # Nur eingeloggte Nutzer dürfen Hunde anlegen
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

        return redirect(url_for("plans"))

    return render_template("plans.html")


@app.route("/plans/all")
def plans_all():
    return render_template("plans_all.html")


if __name__ == "__main__":
    app.run(debug=True)
