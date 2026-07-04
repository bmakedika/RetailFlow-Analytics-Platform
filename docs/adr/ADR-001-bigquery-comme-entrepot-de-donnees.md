# ADR-001 - BigQuery comme entrepôt de données

## Statut

Accepté

## Date

2026-06-21

## Contexte

Le projet nécessite un entrepôt de données capable de stocker et d'interroger des volumes importants de données e-commerce (commandes, clients, produits, paiements). Plusieurs options ont été évaluées : PostgreSQL, SQLite et BigQuery.

## Décision

Utiliser **Google BigQuery** comme entrepôt de données central.

## Justification

- Scalabilité native sans gestion d'infrastructure serveur
- Connexion native avec DBT (`dbt-bigquery`)
- Séparation naturelle des couches raw / staging / marts via les datasets GCP
- Compétence très demandée sur le marché data en France
- Gratuit jusqu'à 10 Go de stockage et 1 To de requêtes par mois (free tier)

## Conséquences

- Nécessite un compte GCP et une clé de service account
- Les credentials doivent être gérés via `GOOGLE_APPLICATION_CREDENTIALS` (hors repo)
- Dépendance à un service cloud propriétaire (GCP)
