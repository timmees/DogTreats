# DogTreats – Personalized Dog Subscription Web App

DogTreats is a full-stack web application that creates personalized dog food and snack subscription models based on a dog’s breed, age, size, and individual sensitivities. The system focuses on organic, locally sourced products and flexible subscription management.

This project was developed as part of the course **Full Stack Web Development**  
by **Prof. Dr. Alexander Eck**.

**Project by:** Tim Mees & Paul Jauert

---

## Features

- User registration and login system
- Session-based authentication
- Create and manage multiple dogs per userrss
- Intelligent recommendation system for subscription models
- Dynamic subscription calculation based on dog weight and needs
- Shopping cart stored in session
- Adjustable delivery intervals
- Subscription management (pause, resume, cancel)
- Product overview with category structure
- SQLite database backend

---

## Technologies Used

| Technology | Description |
|------------|-------------|
| Python     | Backend logic |
| Flask      | Web framework |
| SQLite     | Lightweight relational database |
| Jinja2     | HTML templating |
| HTML/CSS   | Frontend layout and styling |

---

## Core Design Decisions

- Flask + SQLite for a lightweight and transparent MVP architecture
- Service-based backend structure for clean separation of concerns
- Session-based cart and authentication handling
- Rule-based recommendation logic instead of machine learning
- Subscription-first business model instead of single product purchases
- Modular backend services for maintainability and extensibility

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/timmees/dogtreats.git
cd dogtreats
```
### 2. Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

### 3. Install flask
pip install flask

### 4. Initialize Database
sqlite3 dogtreats.db < schema.sql
sqlite3 dogtreats.db < schema_products.sql
sqlite3 dogtreats.db < seed_products.sql

### 5. Run Application
python app.py
```md
Open in browser: http://127.0.0.1:5000
---
## Database Structure

Main tables:

- `users` – registered users  
- `dogs` – user-owned dogs  
- `products` – product catalog  
- `categories` – product categories  
- `subscriptions` – active dog subscriptions  

---

## Subscription Logic

Subscriptions are generated dynamically based on:

- Dog weight  
- Dog age  
- Breed  
- Sensitivities and allergies  

The recommendation system selects suitable products and calculates:

- Daily food consumption  
- Weekly food requirement  
- Subscription size and pricing  
- Recommended delivery intervals  

---

## Future Extensions

- Payment system integration  
- Email notifications for deliveries  
- Advanced nutrition recommendations

