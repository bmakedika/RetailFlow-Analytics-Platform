# ADR-003 - DBT pour la transformation des données

## Statut

Accepté

## Date

2026-06-25

## Contexte

Une fois les données chargées dans BigQuery (couche `raw`), elles doivent être nettoyées, typées et agrégées en tables métier. Plusieurs approches ont été envisagées : scripts SQL manuels, scripts Python avec Pandas, ou DBT.

## Décision

Utiliser **DBT Core** pour toutes les transformations.

## Justification

- Transformations écrites en SQL standard, lisibles et maintenables
- Tests de qualité intégrés (not_null, unique, accepted_values) sans code supplémentaire
- Documentation automatique des modèles et des colonnes
- Séparation claire des couches : `staging` (nettoyage) → `marts` (agrégations métier)
- Standard moderne très apprécié des recruteurs et des équipes data

## Conséquences

- `profiles.yml` doit être stocké dans `~/.dbt/` (hors repo) pour protéger les credentials
- Chaque modification de logique métier passe par un modèle DBT versionné
- `dbt-bigquery` doit être installé séparément (`pip install dbt-bigquery`)
