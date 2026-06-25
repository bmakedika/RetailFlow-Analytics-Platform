![CI](https://github.com/ton-repo/actions/workflows/ci.yml/badge.svg)

# RetailFlow Analytics Platform

Plateforme data e-commerce qui ingère, transforme et expose des indicateurs métier à partir de données brutes : pipeline GCP, modélisation DBT et dashboard Streamlit.

---

## Contexte & Objectif

Les entreprises e-commerce génèrent de grandes quantités de données (commandes, clients, produits), mais ces données restent souvent difficilement exploitables faute d'infrastructure analytique adaptée. Ce projet s'appuie sur le dataset public du magasin **Olist**, représentatif d'une activité e-commerce réelle, pour simuler un contexte professionnel.

L'objectif : construire une plateforme data moderne permettant de

- ingérer automatiquement les données e-commerce,
- structurer et transformer ces données,
- produire des indicateurs analytiques fiables,
- exposer ces indicateurs via une interface utilisateur.

---

## Architecture

```text
CSV (Olist)
    │
    ▼
Ingestion Python  ──────────────►  BigQuery (raw)
                                         │
                                         ▼
                                  DBT (staging → marts)
                                         │
                                         ▼
                                  Streamlit (dashboard)
```

---

## Stack technique

| Outil                   | Rôle                                          |
|-------------------------|-----------------------------------------------|
| Python                  | Scripts d'ingestion                           |
| BigQuery                | Entrepôt de données                           |
| DBT                     | Modélisation et tests de qualité des données  |
| Streamlit               | Dashboard de visualisation                    |
| Docker / Docker Compose | Conteneurisation et orchestration des services|
| GitHub Actions          | CI/CD                                         |

---

## Avancement & Roadmap

| Composant | État |
| --- | --- |
| Ingestion CSV → BigQuery (Python) | ✅ Fonctionnel |
| Modélisation DBT (staging → marts) + tests qualité | 🔜 À venir |
| Dashboard Streamlit | 🔜 À venir |
| Conteneurisation Docker Compose complète | 🔜 À venir |
| CI/CD GitHub Actions | 🔜 À venir |

---

## Installation & Utilisation

### Prérequis

- Docker et Docker Compose installés
- Un projet GCP avec BigQuery activé
- Une clé de service account GCP au format JSON

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd RetailFlow-Analytics-Platform
```

### 2. Configurer les credentials GCP

Placer votre clé de service account en local (hors du repo, par exemple `~/.gcp/retailflow-sa.json`), puis exporter la variable d'environnement :

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/chemin/vers/votre-cle.json"
```

### 3. Lancer la plateforme avec Docker Compose

```bash
docker compose up --build
```

> **État actuel** : seul le service d'ingestion est pleinement fonctionnel. Les services DBT et Streamlit seront activés dans `docker-compose.yml` au fur et à mesure de leur implémentation.

### 4. Lancer l'ingestion manuellement (hors Docker)

```bash
pip install -r requirements.txt
python ingestion/load_to_bigquery.py
```

### 5. Lancer les tests de qualité DBT

```bash
cd dbt_project
dbt test
```

---

## Structure du projet

```text
RetailFlow-Analytics-Platform/
├── data/
│   └── raw/                                       # fichiers CSV bruts
├── ingestion/
│   └── load_to_bigquery.py                        # pipeline ingestion v1
├── docs/
│   └── RetailFlow_Analytics_Platform_Backlog.pdf  # backlog agile
├── dbt_project/                                   # transformation (à venir)
├── streamlit_app/                                 # dashboard (à venir)
├── requirements.txt
└── README.md
```

---

## Dataset & Documentation

- **Source des données** : [Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Backlog produit** : [`docs/RetailFlow_Analytics_Platform_Backlog.pdf`](docs/RetailFlow_Analytics_Platform_Backlog.pdf)
