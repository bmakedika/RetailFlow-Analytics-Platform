# KPI Catalog

## KPI-001

Nom : Chiffre d'affaires

Calcul : `SUM(total_revenue)`

Table source : `fct_orders`

Statut : ✅ Implémenté

---

## KPI-002

Nom : Nombre de commandes

Calcul : `COUNT(order_id)`

Table source : `fct_orders`

Statut : ✅ Implémenté

---

## KPI-003

Nom : Nombre de clients

Calcul : `COUNT(DISTINCT customer_id)`

Table source : `dim_customers`

Statut : ✅ Implémenté

---

## KPI-004

Nom : Panier moyen

Calcul : `CA / Nombre de commandes`

Table source : `fct_orders`

Statut : 🔜 Roadmap (court terme)

---

## KPI-005

Nom : Top Produits

Calcul : `Classement par revenu généré`

Table source : `dim_products`

Statut : 🔜 Roadmap (court terme)

---

## KPI-006

Nom : Répartition géographique

Calcul : `CA par État`

Table source : `dim_customers`

Statut : 🔜 Roadmap (moyen terme)
