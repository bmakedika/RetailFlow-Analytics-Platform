# Guide de contribution

Ce document décrit comment installer le projet en local, les conventions de code et les règles de contribution.

---

## Prérequis

- Python 3.12
- Docker & Docker Compose
- Un projet GCP avec BigQuery activé
- Une clé de service account GCP au format JSON
- DBT Core installé (`pip install dbt-bigquery`)

---

## Installation en local

### 1. Cloner le projet

```bash
git clone https://github.com/bmakedika/RetailFlow-Analytics-Platform.git
cd RetailFlow-Analytics-Platform
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Copier le template et renseigner les valeurs :

```bash
cp .env.example .env
```

```env
GCP_PROJECT_ID=your_project_id
DATASET=ecommerce_staging
GOOGLE_APPLICATION_CREDENTIALS=/chemin/vers/votre-cle.json
```

### 5. Configurer DBT

Le fichier `profiles.yml` doit être placé en dehors du repo pour des raisons de sécurité :

```bash
mkdir -p ~/.dbt
```

Créer `~/.dbt/profiles.yml` :

```yaml
retailflow:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: service-account
      project: your_project_id
      dataset: ecommerce_staging
      keyfile: /chemin/vers/votre-cle.json
      threads: 4
      timeout_seconds: 300
```

---

## Lancer le projet

### Avec Docker

```bash
docker compose up --build
```

### En local (sans Docker)

```bash
# Ingestion
python ingestion/load_to_bigquery.py

# Transformation DBT
cd dbt_project
dbt run
dbt test

# Dashboard
streamlit run streamlit_app/app.py
```

Accès au dashboard :

```
http://localhost:8501
```

---

## Tests

### Tests unitaires (ingestion)

```bash
pytest tests/
```

### Tests de qualité DBT

```bash
cd dbt_project
dbt test
```

---

## Conventions de code

- **Python** : PEP 8, noms de variables en `snake_case`
- **DBT** : modèles nommés `stg_` pour le staging, `fct_` pour les faits, `dim_` pour les dimensions
- **Variables d'environnement** : toujours via `.env`, jamais en dur dans le code
- **Secrets** : `profiles.yml` dans `~/.dbt/`, clé GCP hors du repo

---

## Conventions de commit

Ce projet suit le standard [Conventional Commits](https://www.conventionalcommits.org/).

Format :

```
type(scope): description courte
```

| Type | Usage |
|---|---|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Modification de documentation |
| `refactor` | Refactoring sans changement de comportement |
| `test` | Ajout ou modification de tests |
| `chore` | Tâches techniques (dépendances, config, gitignore) |

Exemples :

```bash
feat(ingestion): add multi-table pipeline with dynamic file mapping
fix(streamlit): correct import path for Docker compatibility
docs(readme): add project structure section
refactor(dbt): standardize customer_unique_id naming in staging layer
test(dbt): add data quality tests for marts models
chore(gitignore): ignore logs, secrets and dbt artifacts
```

---

## Structure du projet

```
RetailFlow-Analytics-Platform/
├── data/
│   └── raw/                    # fichiers CSV bruts (Olist)
├── ingestion/
│   └── load_to_bigquery.py     # pipeline d'ingestion
├── dbt_project/                # transformation DBT
│   └── models/
│       ├── staging/
│       └── marts/
├── streamlit_app/              # dashboard
│   ├── app.py
│   └── bigquery_client.py
├── tests/                      # tests unitaires
├── docs/                       # documentation projet
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker-compose.yml
├── requirements.txt
└── README.md
```
