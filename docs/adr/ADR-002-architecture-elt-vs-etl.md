# ADR-002 - Architecture ELT plutôt qu'ETL

## Statut

Accepté

## Date

2026-06-21

## Contexte

Deux approches sont possibles pour structurer le pipeline de données :
- **ETL** (Extract → Transform → Load) : transformer les données avant de les charger
- **ELT** (Extract → Load → Transform) : charger les données brutes puis transformer en place

## Décision

Adopter une architecture **ELT**.

## Justification

- BigQuery est suffisamment puissant pour exécuter les transformations directement en SQL
- Les données brutes sont conservées dans la couche `raw`, ce qui garantit la traçabilité et permet de rejouer les transformations à tout moment
- DBT est conçu pour fonctionner dans une architecture ELT
- Découplage clair entre l'ingestion (Python) et la transformation (DBT)

## Conséquences

- La couche `raw` contient des données non nettoyées - elle ne doit pas être exposée directement
- Toute correction de transformation se fait dans DBT sans retoucher l'ingestion
- Le stockage BigQuery est légèrement plus élevé (données brutes conservées)
