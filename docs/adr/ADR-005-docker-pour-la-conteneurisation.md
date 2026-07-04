# ADR-005 - Docker pour la conteneurisation

## Statut

Accepté

## Date

2026-06-27

## Contexte

Le projet doit être reproductible sur n'importe quel environnement (local, CI/CD, serveur). Sans conteneurisation, les dépendances Python, les versions et la configuration varient selon la machine.

## Décision

Utiliser **Docker et Docker Compose** pour conteneuriser les services du projet.

## Justification

- Reproductibilité garantie : même comportement en local, en CI et en production
- Isolation des services : ingestion et Streamlit dans des conteneurs séparés
- Docker Compose orchestre les services et les volumes en une seule commande (`docker compose up --build`)
- Standard incontournable en entreprise pour le déploiement de pipelines data

## Conséquences

- Docker et Docker Compose doivent être installés sur la machine hôte
- Les credentials GCP sont injectés via variable d'environnement (`GOOGLE_APPLICATION_CREDENTIALS`)
- Le fichier `.env` ne doit jamais être versionné (ajouté au `.gitignore`)
