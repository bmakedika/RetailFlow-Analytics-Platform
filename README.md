# RetailFlow Analytics Platform


## Aperçu

La plateforme RetailFlow Analytics est un projet de data engineering clé en main conçu pour simuler une pile de données moderne pour l'analyse du e-commerce.

---

## Contexte & Objectif

Les entreprises e-commerce génèrent de grandes quantités de données (commandes, clients, produits), mais ces données restent souvent difficilement exploitables faute d'infrastructure analytique adaptée. Ce projet s'appuie sur le dataset public **Olist**, représentatif d'une activité e-commerce réelle, pour simuler un contexte professionnel.

L'objectif : construire une plateforme data moderne permettant de

- ingérer automatiquement les données e-commerce,
- structurer et transformer ces données,
- produire des indicateurs analytiques fiables,
- exposer ces indicateurs via une interface utilisateur.

---

## Architecture

```
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

| Outil | Rôle |
|---|---|
| Python | Scripts d'ingestion |
| BigQuery | Entrepôt de données |
| DBT | Modélisation et tests de qualité des données |
| Streamlit | Dashboard de visualisation |
| Docker / Docker Compose | Conteneurisation et orchestration des services |
| GitHub Actions | CI/CD |

---

## Structure du projet

```text
retailflow/
├── data/
│   └── raw/                                       # fichiers CSV bruts
├── ingestion/
│   └── load_to_bigquery.py                        # pipeline ingestion v1
├── docs/
│   └── RetailFlow_Analytics_Platform_Backlog.pdf  # backlog agile
├── dbt_project/                                    # transformation (à venir)
├── streamlit_app/                                  # dashboard (à venir)
├── requirements.txt
└── README.md
```
---

```md
## Dataset

- Olist Brazilian E-Commerce Public Dataset
- Contient : commandes, clients, produits, paiements

---

## Gestion de projet

Projet structuré selon une approche Agile :
- backlog produit défini
- user stories techniques et métier
- progression par versions (v1 → v2 → v3)

---

## Installation & Utilisation

### Prérequis
- Docker et Docker Compose installés
- Un projet GCP avec BigQuery activé
- Une clé de service account GCP au format JSON

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd retailflow
```

### 2. Configurer les credentials GCP

Placer votre clé de service account quelque part en local (hors du repo, par exemple `~/.gcp/retailflow-sa.json`), puis exporter la variable d'environnement :

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/chemin/vers/votre-cle.json"
```

### 3. Lancer la plateforme avec Docker Compose

```bash
docker compose up --build
```

Cette commande démarre les services du pipeline (ingestion, transformation DBT, dashboard Streamlit) tels que définis dans `docker-compose.yml`.

> **Note sur l'avancement actuel** : `dbt_project/` et `streamlit_app/` sont encore en cours de développement (voir [Avancement & Roadmap](#avancement--roadmap)). Aujourd'hui, seul le service d'ingestion est pleinement fonctionnel ; les autres services seront activés dans `docker-compose.yml` au fur et à mesure de leur implémentation.

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

## Avancement & Roadmap

- ✅ Ingestion de données CSV vers BigQuery avec Python
- 🔜 Modélisation DBT (staging → marts) et tests de qualité associés
- 🔜 Dashboard Streamlit
- 🔜 Conteneurisation complète avec Docker Compose (ingestion + DBT + Streamlit)
- 🔜 CI/CD avec GitHub Actions

---

# Valeur du projet

Ce projet démontre :
- la construction de pipelines data
- l’utilisation du cloud (GCP)
- la modélisation analytique
- la mise en place d’une architecture moderne
