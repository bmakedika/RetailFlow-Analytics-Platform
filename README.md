# RetailFlow Analytics Platform

Plateforme data e-commerce permettant de transformer des données brutes en indicateurs métier exploitables — via un pipeline ELT moderne sur GCP.

---

## Présentation

RetailFlow Analytics Platform ingère, transforme et visualise des données e-commerce afin de produire des KPI actionnables pour les équipes métier.

Le projet suit une architecture **ELT** (Extract → Load → Transform) :

| Étape | Outil |
|---|---|
| Ingestion | Python → BigQuery |
| Transformation | DBT (staging & marts) |
| Visualisation | Streamlit |
| Orchestration | Docker |

---

## Architecture

```
CSV (Olist)
    ↓
Ingestion Python
    ↓
BigQuery (raw)        ← données brutes
    ↓
DBT (staging)         ← nettoyage & typage
    ↓
DBT (marts)           ← modélisation métier
    ↓
Streamlit Dashboard   ← visualisation KPI
```

---

## Stack technique

| Outil | Rôle |
|---|---|
| Python 3.12 | Ingestion et scripts |
| BigQuery (GCP) | Entrepôt de données |
| DBT Core | Transformation & tests qualité |
| Streamlit | Dashboard interactif |
| Docker & Docker Compose | Conteneurisation |
| GitHub Actions | CI/CD |

---

## Pipeline de données

### 1. Ingestion

- Chargement automatisé des fichiers CSV vers BigQuery
- Gestion des erreurs et logs structurés
- Pipeline modulaire et scalable

### 2. Transformation (DBT)

- **Staging** : nettoyage et correction des types
- **Marts** : modélisation orientée métier

Tables produites :

| Table | Description |
|---|---|
| `fct_orders` | Faits commandes |
| `dim_customers` | Dimension clients |
| `dim_products` | Dimension produits |

### 3. KPI métier

| KPI | Description |
|---|---|
| Chiffre d'affaires (CA) | Revenu total généré |
| Nombre de commandes | Volume d'activité |
| Nombre de clients | Base clients active |

---

## Dashboard

Dashboard Streamlit connecté à BigQuery :

- Filtres interactifs par période
- Visualisation temporelle des KPI
- Métriques clés : CA, commandes, clients actifs

---

## Insights métier

- Analyse de la croissance du chiffre d'affaires
- Identification des tendances de ventes
- Évolution du nombre de clients actifs
- Base analytique pour la segmentation produit et client

---

## Installation & Utilisation

### Prérequis

- Docker et Docker Compose installés
- Un projet GCP avec BigQuery activé
- Une clé de service account GCP au format JSON

### Variables d'environnement

Créer un fichier `.env` à la racine :

```env
GCP_PROJECT_ID=your_project_id
DATASET=ecommerce_staging
GOOGLE_APPLICATION_CREDENTIALS=/chemin/vers/votre-cle.json
```

### Lancer avec Docker

```bash
docker compose up --build
```

Accès au dashboard :

```
http://localhost:8501
```

### Lancer en local (sans Docker)

```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

---

## CI/CD

- Tests automatisés à chaque push
- Pipeline GitHub Actions
- Badge CI dans le README

---

## Améliorations futures

| Amélioration | Horizon |
|---|---|
| CA mensuel | Court terme |
| Top produits | Court terme |
| Répartition géographique | Moyen terme |
| Panier moyen | Moyen terme |
| UI avancée | Long terme |

---

## Conclusion

Ce projet démontre comment des données e-commerce brutes peuvent être transformées en indicateurs métier actionnables grâce à des outils modernes de data engineering.

---

## Licence

MIT — voir [LICENSE](LICENSE)

---

## Auteur

**Bienvenu MAKEDIKA MAKUALA**
