# Dokumentation und Ressourcen – Projekt „DogTreats“

## **13.11.2025**
- Erste Ideenbesprechung und Brainstorming
- Identifikation zentraler Probleme und Anforderungen
- Festlegung des Teamnamens: **PetTreats**
- Einrichtung der Kommunikationskanäle: Discord und WhatsApp
- Erstellung eines GitHub-Repositories

**Genutzte Ressourcen:**
- [Getting started with Git and GitHub workflows](https://hwrberlin.github.io/fswd/git.html#51-enable-pages-and-configure-the-web-page) – Alexander Eck, letzter Zugriff: 13.11.2025

---

## **24.11.2025**
- Konkretisierung der Projektidee: Spezialisierung auf Hundefutter und Ernährungspläne
- Umbenennung auf "DogTreats"

---

## **26.11.2025**
- Erstellung der SQLite-Datenbank mit den Tabellen **users** und **dogs**
- Einführung in SQLite-Datenbanken
- Einführung in Flask-Routing
- Einführung in Login-, Registrierungs- und Sessionverwaltung

**Genutzte Ressourcen:**
- [Flask SQLite database](https://pythonbasics.org/flask-sqlite/) – pythonbasics.org, letzter Zugriff: 27.11.2025
- [Python and Flask – Routing and Variable Rules](https://www.youtube.com/watch?v=f085KDOy43k) – TheCodex, letzter Zugriff: 27.11.2025
- [How to add Authentication to your App with Flask](https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask/) – GeeksforGeeks, letzter Zugriff: 02.12.2025
- [Flask Python Registration doesn't work properly](https://stackoverflow.com/questions/40237394/flask-python-registration-doesnt-work-properly) – StackOverflow, letzter Zugriff: 02.12.2025
- [How to generate dynamic urls in flask?](https://stackoverflow.com/questions/35107885/how-to-generate-dynamic-urls-in-flask) - StackOverflow, letzter Zugriff: 08.02.2026

**Genutzte KI-Ressourcen**
- [SQl Schema](https://chatgpt.com/share/6988da22-f44c-8002-9beb-05a6aba47153) (nicht so benutzt sondern abgewandelt)

---

## **27.11.2025**
- Erstellung der zentralen `app.py` mit ersten Flask-Routen
- Implementierung erster HTML-Templates:
  - `index.html` – Startseite
  - `base.html` – Layout-Template
  - `profile.html` – Login & Registrierung
  - `plans.html` – Hund anlegen (später `create_dog.html`)

---

## **02.12.2025**
- Implementierung der Session-Verwaltung
- Umsetzung der Login- und Registrierungslogik

---

## **03.12.2025**
- Implementierung des CSS-Designs für ein einheitliches Layout

**Genutzte Ressourcen:**
- [HTML Styles – CSS](https://www.w3schools.com/html/html_css.asp) – W3Schools, letzter Zugriff: 20.01.2026

---

## **11.12.2025**
- Erstellung von neuen Routen -> Zwischenabgabe 
- Implementierung folgender HTML-Templates:
  - `create_dog.html` – Name, Hunderasse, Alter, Gewicht, Allergien/Besonderheiten
  - `impressum.html` – Pseudo-Impressum
  - `kontakt.html` – Pseudo-Kontakt
  - `manage_subscriptions.html` – Platzhalter, später Abos verwalten
  - `mydogs.html` – Platzhalter, später erstellte Hunde ansehen
  - `order_history.html` – Platzhalter, später Bestellhistorie ansehen
  - `track_orders.html` – Platzhalter, später Bestellungen verfolgen

---

## **02.01.2026**

- Erstellte Hunde sowie alle Produkte sind jetzt in den jeweiligen HTML-Templates aufrufbar
- Implementierung von neuem CSS-Designs
- Implementierung folgender SQL-Dateien:
  - `schema_products.sql` – Tabellen "categories" und products" angelegt
  - `seed_products.html` – Tabelle "products" gefüllt
- Implementierung folgender HTML-Templates:
  - `all_products.html` – Einträge aus "products" werden angezeigt
  - `mydogs.html` – erstellte Hunde werden jetzt angezeigt

**Genutzte Ressourcen:**
- [HTML Styles – CSS](https://www.w3schools.com/html/html_css.asp) – W3Schools, letzter Zugriff: 20.01.2026
- [CSS-Grid Layout](https://www.w3schools.com/css/css_grid.asp) – W3Schools, letzter Zugriff: 20.01.2026
- [SQLite-Setup, INSERT INTO, cur.execute, fetchall(), render_template, ](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application) – digitalocean, letzter Zugriff: 10.01.2026
- [Weiteres Tutorial für render_template mit Daten](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-and-sqlite) – digitalocean, letzter Zugriff: 10.01.2026

**Genutzte KI-Ressourcen:**
- [Beispielprojekt](https://chatgpt.com/share/6988d87b-3270-8002-a4f6-d2e4dad51a3d) 

---


## **06.01.2026-10.01.2026**

- Abo-Auswahl basierend auf Hund-Daten implementiert
- POST-Request verarbeitet ausgewählten Hund
- Berechnung von `grams_per_day` basierend auf Gewicht (20g pro kg)
- Produktempfehlung abhängig von Allergien/Sensitivitäten 

Implementierung folgender HTML-Templates:
 - `plans_all.html` – Hunde Auswahl`<select>` Dropdown, Abo-Vorschläge
 - `cart.html` - noch keine Logik

**Genutzte Ressourcen:**
- [Dropdown - Auswahl](https://csveda.com/flask-and-mysql-how-to-fill-table-data-in-a-dropdown/) – csveda, letzter Zugriff: 10.01.2026
- [SQLite-Setup, INSERT INTO, cur.execute, fetchall(), render_template, ](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application) – digitalocean, letzter Zugriff: 10.01.2026
- [Weiteres Tutorial für render_template mit Daten](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-and-sqlite) – digitalocean, letzter Zugriff: 10.01.2026
- [HTML Styles – CSS](https://www.w3schools.com/html/html_css.asp) – W3Schools, letzter Zugriff: 20.01.2026


## **15.01.2026**
- Session-basierter Warenkorb implementiert - `cart.html`
- Lieferinterval wird pro Warenkorb-Item in der Flask-Session gespeichert
- Implementierung von `delivery_interval.html`

**Genutzte Ressourcen:**
- [Beispiel eines Warenkorbes mit Session](https://helperbyte.com/questions/12319/how-you-can-implement-a-shopping-cart-using-sessions-in-flask) – Hyperbyte, letzter Zugriff: 15.01.2026

## **19.01.2026-20.01.206**

- Abo-Features implementiert (hinzufügen, anzeigen, pausieren, löschen)
- Warenkorb leeren
- neue Struktur: Core-Features ausgelagert: Warenkorb (`cart_service.py`), Abo-Modell-Zusammenstellung (`plans_service.py`), Abo-Verwaltung (`subs_service.py`) -> `app.py` nur noch Routes mit dazugehöriger Logik
- Abo-Zusammenstellung basierend auf Punktesystem, welches von Hund-Attributen abhängig ist
- Implementierung von `checkout.html`

**Genutzte Ressourcen:**
- [SQLite-Setup, INSERT INTO, cur.execute, fetchall(), render_template](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application) – digitalocean, letzter Zugriff: 03.01.2026

**Genutzte KI-Ressourcen:**
-[Route-Example](https://chatgpt.com/share/6988e0fe-b968-8002-bebe-f941a6f300d7)
---

## **20.01.2026**
- Vorschaubilder für Abo-Modelle implementiert

---

## **21.01.2026**
- kleine Verbesserungen (Code optimiert, Kommentare hinzugefügt)

---

## **04.02.2026**
- Flash-Message Pop-Up, wenn Abo abgeschlossen wird
- `profile.html`: Redesign mit vorhandener CSS-Klasse "product-Card" 

**Genutzte Ressourcen:**
- [Message Flashing](https://flask.palletsprojects.com/en/stable/patterns/flashing/) - flask.palletprojects, letzter Zugriff: 04.02.2026
- [Flask Tutorial #6 - Message Flashing](https://www.youtube.com/watch?v=qbnqNWXf_tU) – Tech With Tim, letzter Zugriff: 04.02.2026

---
## **08.02.2026**

- Simulierte Bestellverfolgung implementiert:
  - Status-Updates basierend auf vergangener Zeit -> `order_date`
  - Zeitbasierte Logik: `timedelta` und `.total_seconds()`
  - 4 Status-Stufen:
    - **In Vorbereitung** (0-24h nach Bestellung)
    - **Versendet** (24-48h nach Bestellung)
    - **Zustellung** (48-72h nach Bestellung)
    - **Bestellung abgeschlossen** (72h+ nach Bestellung)
  - Berechnung für Simulation: `hours_since_order = (now - order_date).total_seconds() / 3600`

Aktuallisierung folgender HTML-Templates:
- `Orders` – Bestellhistorie
- `track_orders` – Zusammenfassung der Bestellung + Bestellfortschritt

**Genutzte Ressourcen:**
- [Python timedelta: Working With Time Intervals in Python](https://www.datacamp.com/tutorial/timedelta-python-time-intervals) - Stephen Gruppetta, letzter Zugriff: 08.02.2026
- [datetime.timedelta() function - Python](https://www.geeksforgeeks.org/python/python-datetime-timedelta-function/) - geeksforgeeks, letzter Zugriff: 08.02.2026
- [Convert Between Isoformat String and datetime in Python](https://note.nkmk.me/en/python-datetime-isoformat-fromisoformat/) - note.nkmk.me, letzter Zugriff: 08.02.2026
- [Python DateTime Format Using Strftime()](https://pynative.com/python-datetime-format-strftime/) - pynative, letzter Zugriff: 08.02.2026

**Genutzte KI-Quellen**
-[Code-Optimisation in plans_service.py](https://claude.ai/share/e13dc79c-d8e1-4c43-b343-8f5e124f90d3) 

---
