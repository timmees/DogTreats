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

## **02.01.2ß26**

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
- [SQLite-Setup, INSERT INTO, cur.execute, fetchall(), render_template, ](https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application) – digitalocean, letzter Zugriff: 03.01.2026
- [Weiteres Tutorial für render_template mit Daten](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-and-sqlite) – digitalocean, letzter Zugriff: 03.01.2026

---


## **06.01.2026**






 