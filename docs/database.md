# Datenbank-Dokumentation 

---

## users
- `username` (PK, String)  
- `password_hash` (String) (Hinweis: noch kein Hash implementiert)

---

## dogs
- `id` (PK, Int)  
- `username` (FK → users.username, String)  
- `name` (String)  
- `breed` (String)  
- `age_years` (Int, optional)  
- `weight_kg` (Float, optional)  
- `sensitivities` (String, optional)  

---

## subscriptions

- `id` (PK, Int)  
- `username` (FK → users.username, String)  
- `dog_name` (String)  
- `plan_title` (String)  
- `interval_days` (Int)  
- `price` (Float)  
- `is_paused` (Boolean/Int, Default 0)  
- `pause_until` (Date, optional)  
- `created_at` (DateTime, Default CURRENT_TIMESTAMP)  

---

## categories
> wird im Query `JOIN categories c ON p.category_id = c.id` verwendet.

- `id` (PK, Int)  
- `name` (String)  

---

## products
>   wird verwendet in(`all_products`, `plans_service.get_product`).

- `id` (PK, Int)  
- `name` (String)  
- `description` (String)  
- `origin` (String, optional)  
- `quality_notes` (String, optional)  
- `base_amount_g` (Int)  
- `base_price_eur` (Float)  
- `image_url` (String, optional)  
- `category_id` (FK → categories.id, Int)  

---
