# Documentation - RetailFlow Analytics Platform

Ce dossier contient l'ensemble de la documentation du projet, organisée en trois catégories.

---

## Gouvernance

| Fichier | Description |
|---|---|
| [`gouvernance/project_character.md`](gouvernance/project_character.md) | Project Charter : contexte, vision, objectifs et critères de succès |
| [`gouvernance/business_case.md`](gouvernance/business_case.md) | Business Case : situation actuelle, situation cible et bénéfices attendus |
| [`gouvernance/glossaire.md`](gouvernance/glossaire.md) | Glossaire des termes techniques et métier du projet |

---

## Produit

| Fichier | Description |
|---|---|
| [`product/personas.md`](product/personas.md) | Personas : profils utilisateurs et leurs objectifs |
| [`product/kpi_catalog.md`](product/kpi_catalog.md) | Catalogue des KPIs : formules, tables sources et statut d'implémentation |
| [`product/data_dictionary.md`](product/data_dictionary.md) | Data Dictionary : description des tables staging et marts |
| [`RetailFlow_Analytics_Platform_v0.5.pdf`](RetailFlow_Analytics_Platform_v0.5.pdf?raw=true) | Product Backlog complet : EPICs, user stories, sprints, architecture et roadmap |

---

## Architecture Decision Records (ADR)

Les ADR documentent les décisions techniques structurantes du projet.

| Fichier | Décision |
|---|---|
| [`adr/ADR-001-bigquery-comme-entrepot-de-donnees.md`](adr/ADR-001-bigquery-comme-entrepot-de-donnees.md) | Choix de BigQuery comme entrepôt de données |
| [`adr/ADR-002-architecture-elt-vs-etl.md`](adr/ADR-002-architecture-elt-vs-etl.md) | Choix d'une architecture ELT plutôt qu'ETL |
| [`adr/ADR-003-dbt-pour-la-transformation.md`](adr/ADR-003-dbt-pour-la-transformation.md) | Choix de DBT pour la transformation des données |
| [`adr/ADR-004-streamlit-pour-la-visualisation.md`](adr/ADR-004-streamlit-pour-la-visualisation.md) | Choix de Streamlit pour la visualisation |
| [`adr/ADR-005-docker-pour-la-conteneurisation.md`](adr/ADR-005-docker-pour-la-conteneurisation.md) | Choix de Docker pour la conteneurisation |

---

## Fichiers à la racine du projet

| Fichier | Description |
|---|---|
| [`../README.md`](../README.md) | Présentation générale du projet |
| [`../CHANGELOG.md`](../CHANGELOG.md) | Historique des versions v0.1.0 → v0.4.0 |
| [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Guide d'installation et conventions de contribution |
