# Data Dictionary

Ce document décrit l'ensemble des tables du projet RetailFlow Analytics Platform, organisées par couche : **staging** (nettoyage & typage) et **marts** (agrégations métier).

---

## Couche Staging

Les modèles staging lisent depuis la couche `raw` de BigQuery et appliquent les corrections de types et de nommage. Ils ne contiennent aucune agrégation.

---

### `stg_customers`

**Source** : `retailflow-analytics.ecommerce_raw.customers`

**Description** : Clients de la plateforme Olist après nettoyage et standardisation des identifiants.

| Colonne | Type | Description |
|---|---|---|
| `customer_id` | STRING | Identifiant unique de la commande client (clé primaire) |
| `customer_unique_id` | STRING | Identifiant unique du client physique (un même client peut avoir plusieurs `customer_id`) |
| `zip_code` | STRING | Code postal du client |
| `city` | STRING | Ville du client |
| `state` | STRING | État brésilien du client (ex. SP, RJ) |

---

### `stg_orders`

**Source** : `retailflow-analytics.ecommerce_raw.orders`

**Description** : Commandes passées sur la plateforme avec leurs statuts et timestamps.

| Colonne | Type | Description |
|---|---|---|
| `order_id` | STRING | Identifiant unique de la commande (clé primaire) |
| `customer_id` | STRING | Référence vers `stg_customers.customer_id` |
| `order_status` | STRING | Statut de la commande (delivered, shipped, canceled, etc.) |
| `purchase_ts` | TIMESTAMP | Date et heure d'achat de la commande |
| `delivered_ts` | TIMESTAMP | Date et heure de livraison au client |

---

### `stg_order_items`

**Source** : `retailflow-analytics.ecommerce_raw.order_items`

**Description** : Articles composant chaque commande avec les prix et frais de livraison.

| Colonne | Type | Description |
|---|---|---|
| `order_id` | STRING | Référence vers `stg_orders.order_id` |
| `product_id` | STRING | Référence vers `stg_products.product_id` |
| `seller_id` | STRING | Identifiant du vendeur |
| `price` | FLOAT64 | Prix unitaire de l'article |
| `freight_value` | FLOAT64 | Frais de livraison de l'article |

---

### `stg_products`

**Source** : `retailflow-analytics.ecommerce_raw.products`

**Description** : Catalogue produits de la plateforme avec caractéristiques physiques et catégorie.

| Colonne | Type | Description |
|---|---|---|
| `product_id` | STRING | Identifiant unique du produit (clé primaire) |
| `product_category` | STRING | Catégorie du produit (ex. electronics, furniture) |
| `product_name_length` | FLOAT64 | Longueur du nom du produit (nombre de caractères) |
| `product_description_length` | FLOAT64 | Longueur de la description du produit (nombre de caractères) |
| `product_photos_quantity` | FLOAT64 | Nombre de photos du produit |
| `product_weight` | FLOAT64 | Poids du produit en grammes |
| `product_length` | FLOAT64 | Longueur du produit en centimètres |
| `product_height` | FLOAT64 | Hauteur du produit en centimètres |
| `product_width` | FLOAT64 | Largeur du produit en centimètres |

---

## Couche Marts

Les modèles marts lisent depuis la couche staging et produisent des tables agrégées orientées métier, consommées directement par Streamlit.

---

### `dim_customers`

**Source** : `stg_customers`

**Description** : Dimension clients exposant les informations géographiques pour l'analyse territoriale.

| Colonne | Type | Description |
|---|---|---|
| `customer_id` | STRING | Identifiant unique de la commande client (clé primaire) |
| `customer_unique_id` | STRING | Identifiant unique du client physique |
| `city` | STRING | Ville du client |
| `state` | STRING | État brésilien du client |

---

### `dim_products`

**Source** : `stg_products`

**Description** : Dimension produits exposant les informations catalogue pour l'analyse des performances.

| Colonne | Type | Description |
|---|---|---|
| `product_id` | STRING | Identifiant unique du produit (clé primaire) |
| `product_category` | STRING | Catégorie du produit |
| `product_name_length` | FLOAT64 | Longueur du nom du produit |
| `product_description_length` | FLOAT64 | Longueur de la description du produit |

---

### `fct_orders`

**Source** : `stg_orders` JOIN `stg_order_items`

**Description** : Table de faits agrégée par jour exposant le volume de commandes et le chiffre d'affaires. Table centrale consommée par le dashboard Streamlit.

| Colonne | Type | Description |
|---|---|---|
| `order_date` | DATE | Date de la commande (agrégation journalière) |
| `total_orders` | INTEGER | Nombre de commandes distinctes sur la journée |
| `total_revenue` | FLOAT64 | Chiffre d'affaires total de la journée (SUM des prix articles) |

**Calculs** :

```sql
total_orders  = COUNT(DISTINCT order_id)
total_revenue = SUM(price)
```

---

## Relations entre les tables

```
stg_customers ──────────────────► dim_customers
stg_products  ──────────────────► dim_products
stg_orders    ─┐
               ├── JOIN order_id ─► fct_orders
stg_order_items┘
```
