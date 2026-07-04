# ADR-004 - Streamlit pour la visualisation

## Statut

Accepté

## Date

2026-06-26

## Contexte

Les KPIs produits par DBT doivent être exposés via une interface utilisateur accessible aux équipes métier. Les options évaluées : Power BI, Metabase, Grafana et Streamlit.

## Décision

Utiliser **Streamlit** pour le dashboard de visualisation dans la version MVP.

## Justification

- Développement rapide en Python pur, sans front-end séparé
- Intégration directe avec le client BigQuery Python
- Mise en cache des requêtes via `@st.cache_data` pour optimiser les performances
- Cohérence avec la stack Python du projet (ingestion + DBT + Streamlit)
- Conteneurisable facilement avec Docker

## Conséquences

- Le dashboard nécessite un accès BigQuery actif pour afficher les données
- Streamlit est adapté au MVP mais pourra être remplacé par Power BI en production (roadmap)
- Les credentials GCP doivent être disponibles dans l'environnement d'exécution
