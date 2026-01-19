#Logik für aktive Abos
from datetime import date, timedelta

#Abos des Nutzers aus DB holen, um sie in "Abos verwalten" anzuzeigen 
def subs_list(cur, username):
    cur.execute("""
        SELECT id, dog_name, plan_title, interval_days, price, is_paused, pause_until
        FROM subscriptions
        WHERE username = ?
        ORDER BY created_at DESC
    """, (username,))
    return cur.fetchall()

#Datensatz in subscriptions wird für jedes Warenkorb-Item angelegt
def subs_create_from_cart(cur, username, items):
    for it in items:
        cur.execute("""
            INSERT INTO subscriptions
            (username, dog_name, plan_title, interval_days, price)
            VALUES (?, ?, ?, ?, ?)
        """, (
            username,
            it["dog_name"],
            it["plan_title"],
            it.get("delivery_interval_days", it["days"]),
            it["price"]
        ))

def subs_pause(cur, username, sub_id, pause_days):
    pause_until = date.today() + timedelta(days=pause_days)
    cur.execute("""
        UPDATE subscriptions
        SET is_paused = 1, pause_until = ?
        WHERE id = ? AND username = ?
    """, (pause_until.isoformat(), sub_id, username))

def subs_resume(cur, username, sub_id):
    cur.execute("""
        UPDATE subscriptions
        SET is_paused = 0, pause_until = NULL
        WHERE id = ? AND username = ?
    """, (sub_id, username))

def subs_cancel(cur, username, sub_id):
    cur.execute("""
        DELETE FROM subscriptions
        WHERE id = ? AND username = ?
    """, (sub_id, username))
