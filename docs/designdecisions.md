#

## Design Decision 1: Verwendung von Flask Sessions für Authentifizierung statt Flask-Login

### Context  
Wir benötigen Login/Logout und einen persistenten Login-Zustand über Requests.  
Das Projekt ist klein und hat nur einfache Rollen (keine Admin-/User-Hierarchien).

### Decision  
Verwendung von Flask-`session` für Authentifizierung (`session["username"]`).

### Consequences  
+ einfache Implementierung  
+ Keine zusätzliche Dependency  
+ Volle Kontrolle über Session-Daten  
- Schwerer erweiterbar für komplexere Projekte

### Alternatives Considered  
**Flask-Login**  
+ Standardisierte Lösung  
- Für unser Projekt Overkill

---

## Design Decision 2: Nutzung von SQLite als Datenbank

### Context  
lokales, kleines Projekt ohne hohe Last oder parallele Zugriffe

### Decision  
SQLite als Datenbank

### Consequences  
+ Keine Serverinstallation nötig  
+ Einfaches File-basiertes Setup  
- Schlechte Skalierbarkeit  

### Alternatives Considered  
**MySQL, SQAlchemy**  
+ Skalierbar  
- Höherer Setup-Aufwand

---

## Design Decision 3: Session-basierter Warenkorb statt DB-Warenkorb

### Context  
Der Warenkorb ist temporär, für Nutzer zugeteilt und nur für den Checkout relevant

### Decision  
Speicherung des Warenkorbs in `session["cart"]`

### Consequences  
+ schnelle Implementierung  
+ Kein DB-Schema nötig  
+ Automatische Löschung bei Logout  
- Geht bei Session-Verlust verloren  
- Nicht geräteübergreifend  

### Alternatives Considered  
**DB-basierter Warenkorb**  
+ dauerhafte Speicherung -> gut für Nachvollziehbarkeit  

---

## Design Decision 4: Punktebasierte Abo-Empfehlungslogik statt Machine Learning

### Context  
Abo-Empfehlungen solln abhängig von Attributen des Hundes sein

### Decision  
in Python: (`recommend_plans`).

### Consequences  
+ Verständlich und nachvollziehbar  
+ Schnell implementiert  
+ Leicht anpassbar  

---
## Design Decision 5: Eigenes CSS statt Bootstrap

### Context  
Die Anwendung soll übersichtlich und praktisch sein.

### Decision  
Verwendung von normalem, selbst geschriebenem CSS statt Bootstrap.

### Consequences  
+ Volle Kontrolle über Design und Styling  
+ Keine externe Dependency  
+ Besseres Verständnis von CSS-Grundlagen  

- Mehr eigener Aufwand für Layout & Responsiveness  

### Alternatives Considered  
**Bootstrap**  
+ Schnelles Prototyping  
+ Viele vorgefertigte Komponenten  
- Weniger individuelles Design  
- Zeitlich nicht mehr geschafft umzusetzen
