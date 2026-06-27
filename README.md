# RetailFlow Analytics Platform

[![CI](https://github.com/bmakedika/RetailFlow-Analytics-Platform/actions/workflows/ci.yml/badge.svg)](https://github.com/bmakedika/RetailFlow-Analytics-Platform/actions/workflows/ci.yml)


## Présentation

RetailFlow Analytics Platform est une plateforme data complète permettant d'ingérer, transformer et analyser des données e-commerce afin de produire des indicateurs métier exploitables.

Le projet suit une architecture moderne de type ELT :

- **Ingestion** : Python → BigQuery
- **Transformation** : DBT (staging & marts)
- **Visualisation** : Streamlit
- **Orchestration & Déploiement** : Docker

---

## Architecture

```
CSV (Olist)
    ↓
Ingestion Python
    ↓
BigQuery (raw)
    ↓
DBT (staging)
    ↓
DBT (marts)
    ↓
Streamlit Dashboard
```

---

## Stack technique

- Python 3.12
- BigQuery (GCP)
- DBT Core
- Streamlit
- Docker & Docker Compose
- GitHub Actions (CI/CD)

---

## Arborescence du projet

```
RetailFlow-Analytics-Platform/
├── data/
│   └── raw/                    
├── ingestion/
│   └── load_to_bigquery.py     
├── dbt_project/
│   └── models/
│        └── staging/
│        └── marts/
├── tests/
│   └── test_ingestion.py
├── streamlit_app/  
│   └── app.py
│   └── bigquery_client.py
│   └── Dockerfile
├── docs/
│   └── RetailFlow_Analytics_Platform_Backlog.pdf
├── .github/
│   └── workflow
│       └── ci.yml              
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Pipeline de données

### Ingestion

- Chargement automatisé des fichiers CSV
- Gestion des erreurs et logs
- Pipeline modulaire et scalable

### Transformation (DBT)

- Nettoyage des données (staging)
- Modélisation en tables métiers :
  - `fct_orders`
  - `dim_customers`
  - `dim_products`

### KPI métier

- Chiffre d'affaires (CA)
- Nombre de commandes
- Nombre de clients

---

## Dashboard

Fonctionnalités :

- Filtres interactifs par date
- KPI : commandes, clients, CA
- Visualisation temporelle
- Dashboard connecté à BigQuery

---

## Insights business

- Analyse de la croissance du chiffre d'affaires
- Identification des tendances de ventes
- Évolution du nombre de clients
- Base pour analyse des produits et segmentation

---

## Lancer avec Docker

```bash
docker compose up --build
```

Accès :

```
http://localhost:8501
```

### Variables d'environnement

Créer un fichier `.env` :

```env
GCP_PROJECT_ID=your_project_id
DATASET=ecommerce_staging
GOOGLE_APPLICATION_CREDENTIALS=/chemin/vers/votre-cle.json
```

---

## CI/CD

- Tests automatisés
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

Ce projet démontre la capacité à construire une plateforme data complète allant de l'ingestion des données jusqu'à leur visualisation avec une approche orientée métier.

---

## License

MIT — see [LICENSE](LICENSE)

---

## Auteur

Bienvenu MAKEDIKA MAKUALA
