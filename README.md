# RetailFlow Analytics Platform

## Contexte
Olist est une plateforme e-commerce brésilienne permettant à des vendeurs de distribuer leurs produits sur plusieurs marketplaces.  
Le dataset utilisé représente des transactions réelles (commandes, clients, produits).

## Objectif
Construire une plateforme data moderne permettant :
- d’ingérer des données e-commerce
- de les transformer et structurer
- de produire des indicateurs analytiques

## Réalisations
- Ingestion de données CSV vers BigQuery avec Python
- Modélisation avec DBT (staging → marts)
- Mise en place de tests de qualité (DBT tests)
- Développement d’un dashboard avec Streamlit
- Conteneurisation avec Docker
- CI/CD avec GitHub Actions

## Stack technique
- Python
- SQL
- GCP (BigQuery)
- DBT
- Streamlit
- Docker

## Architecture
data → ingestion → BigQuery → DBT → Streamlit)
