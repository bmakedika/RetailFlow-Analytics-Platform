# RetailFlow Analytics Platform

## Présentation

RetailFlow Analytics Platform est une plateforme de données conçue pour transformer des données e-commerce brutes en indicateurs fiables et exploitables afin d'améliorer la prise de décision commerciale

Le projet met en œuvre une architecture moderne de type ELT permettant d'ingérer, transformer et visualiser des données issues d'une activité de commerce électronique

RetailFlow couvre l'ensemble du cycle de vie de la donnée :

- ingestion automatisée des données
- stockage analytique
- transformation métier
- production de KPI
- visualisation décisionnelle
- industrialisation via Docker

---

## Contexte

Les entreprises e-commerce génèrent quotidiennement de grandes quantités de données : commandes, clients, produits, paiements, livraisons. Bien que ces données soient disponibles, elles restent souvent dispersées dans plusieurs fichiers ou systèmes techniques

Cette situation entraîne :

- une faible visibilité sur les performances
- des analyses manuelles répétitives
- des délais dans la production des rapports
- des difficultés à produire des indicateurs fiables

RetailFlow est né de la volonté de reproduire un cas réel rencontré dans l'univers e-commerce. Le projet s'appuie sur le jeu de données public **Olist** (Kaggle), représentant l'activité d'une marketplace brésilienne. L'objectif n'était pas uniquement d'analyser les données, mais de construire une plateforme Data Engineering complète permettant l'automatisation de l'ingestion, la standardisation des transformations, la production d'indicateurs métier et la visualisation des performances commerciales

---

## Vision

Transformer les données e-commerce en intelligence commerciale afin d'accélérer la prise de décision

---

## Valeur métier

### Visibilité

Obtenir une vision consolidée des ventes et des revenus

### Fiabilité

Garantir des indicateurs cohérents et reproductibles

### Automatisation

Réduire les manipulations manuelles

### Décision

Faciliter l'identification des tendances et opportunités commerciales

---

## Architecture

```
CSV (Olist)  →  Python Ingestion  →  Google BigQuery  →  DBT  →  Data Marts  →  Streamlit / Power BI  →  Décision métier
```

---

## Technologies

- Python
- Google BigQuery
- DBT
- Streamlit
- Docker
- GitHub Actions
- Power BI (roadmap)

---

## Principaux KPI

- Chiffre d'affaires
- Nombre de commandes
- Nombre de clients
- Panier moyen
- Top produits
- Performance géographique

---

## Auteur

Bienvenu MAKEDIKA MAKUALA
