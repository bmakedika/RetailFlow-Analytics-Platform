# Journal des modifications

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et ce projet respecte le [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v0.4.0] - 2026-06-27 — MVP

### Ajouté
- Dashboard Streamlit interactif avec intégration BigQuery et KPIs e-commerce
- Module BigQuery client réutilisable avec mise en cache des requêtes (`@st.cache_data`)
- Visualisation temporelle et filtres par date pour l'exploration des KPIs
- Dockerfile pour le service d'ingestion
- Dockerfile pour le service Streamlit dashboard
- Configuration Docker Compose pour orchestrer tous les services et volumes
- `streamlit_app` défini comme package Python pour les imports de modules
- Template de variables d'environnement (`.env.example`) étendu avec les credentials GCP

### Corrigé
- Chemin d'import corrigé pour la compatibilité en local et dans Docker
- Dépendance `db-dtypes` ajoutée pour la compatibilité BigQuery/Pandas

### Documentation
- README refondu avec architecture, pipeline et insights métier
- Badge CI/CD ajouté
- Section arborescence du projet ajoutée
- Instructions de lancement en local ajoutées
- Backlog v0.4 mis à jour avec la section Roadmap et le storytelling amélioré

---

## [v0.3.0] - 2026-06-25 — Pipeline DBT & CI/CD

### Ajouté
- Projet DBT initialisé avec le profil BigQuery
- Modèles staging : `stg_orders`, `stg_customers`, `stg_products`, `stg_order_items`
- Modèles marts : `fct_orders` (avec calcul du revenu), `dim_customers`, `dim_products`
- Tests de qualité sur tous les modèles staging et marts (not_null, unique, accepted_values)
- Workflow CI GitHub Actions pour les tests automatisés
- Package de tests unitaires initialisé pour le pipeline d'ingestion

### Refactorisé
- Nommage de l'identifiant client standardisé dans les couches staging et marts
- Modèle staging order items simplifié par suppression des colonnes inutilisées

### Documentation
- Fichiers de documentation DBT ajoutés
- Template de variables d'environnement ajouté
- Backlog mis à jour avec l'objectif sous la section vision

---

## [v0.2.0] - 2026-06-22 — Ingestion v2 & Observabilité

### Ajouté
- Pipeline d'ingestion multi-tables avec mapping dynamique des fichiers
- Fonctions pipeline réutilisables pour une ingestion modulaire
- Module de configuration pour externaliser les paramètres via variables d'environnement
- Logging structuré pour le pipeline d'ingestion (fichier + console)
- Gestion des erreurs et logging pour une exécution résiliente du pipeline

### Refactorisé
- Script principal d'ingestion simplifié avec une structure modulaire
- Module d'ingestion initialisé comme package Python

### Documentation
- Flux de lecture du README réorganisé et sections redondantes supprimées
- Nom du repo et ponctuation corrigés

---

## [v0.1.0] - 2026-06-21 — Version initiale

### Ajouté
- Structure du projet initialisée
- Dataset Olist Brazilian E-Commerce ajouté (`data/raw/`)
- Dépendances Python initiales
- Pipeline d'ingestion v1 pour charger un fichier CSV dans BigQuery (`load_to_bigquery.py`)

### Documentation
- README avec contexte, objectifs et aperçu de l'architecture
- Product backlog initial avec EPICs, user stories et story points
