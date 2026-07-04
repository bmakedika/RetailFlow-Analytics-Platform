# Glossaire

Ce document définit les termes métier et techniques utilisés dans le projet RetailFlow Analytics Platform.

---

## Termes techniques

**BigQuery**
Entrepôt de données cloud proposé par Google Cloud Platform (GCP). Il permet de stocker et d'interroger de grands volumes de données via SQL. Dans ce projet, BigQuery héberge les trois couches de données : raw, staging et marts.

**CI/CD (Continuous Integration / Continuous Delivery)**
Pratique de développement qui automatise les tests et la validation du code à chaque modification. Dans ce projet, le pipeline CI/CD est géré par GitHub Actions.

**Data Dictionary**
Document qui décrit la structure des tables d'un projet data : colonnes, types, descriptions et relations. Il sert de référence pour comprendre la signification de chaque champ.

**Data Mart**
Table agrégée et orientée métier, issue de la transformation des données staging. Les marts sont conçus pour répondre à des questions métier précises. Exemples dans ce projet : `fct_orders`, `dim_customers`, `dim_products`.

**DBT (Data Build Tool)**
Outil open source de transformation de données. Il permet d'écrire des transformations SQL versionnées, testées et documentées. DBT opère directement dans l'entrepôt de données (BigQuery) selon une architecture ELT.

**Dimension**
Table contenant les attributs descriptifs d'une entité métier (clients, produits). Dans un schéma en étoile, les dimensions entourent la table de faits. Exemples : `dim_customers`, `dim_products`.

**Docker**
Plateforme de conteneurisation qui permet d'emballer une application et ses dépendances dans un conteneur isolé et reproductible.

**Docker Compose**
Outil permettant de définir et d'orchestrer plusieurs conteneurs Docker via un fichier de configuration (`docker-compose.yml`).

**ELT (Extract → Load → Transform)**
Architecture de pipeline de données où les données sont d'abord extraites de la source, chargées brutes dans l'entrepôt, puis transformées en place. S'oppose à l'ETL où la transformation précède le chargement.

**ETL (Extract → Transform → Load)**
Architecture de pipeline de données où les données sont transformées avant d'être chargées dans l'entrepôt. Approche plus ancienne, remplacée par l'ELT dans les architectures cloud modernes.

**Fact Table (Table de faits)**
Table centrale d'un schéma en étoile contenant les mesures quantitatives d'un processus métier (revenus, volumes). Exemple : `fct_orders`.

**GitHub Actions**
Service d'intégration continue intégré à GitHub. Il exécute automatiquement des workflows (tests, build) à chaque push sur le dépôt.

**Ingestion**
Processus de chargement des données depuis une source (fichiers CSV) vers un système de stockage (BigQuery). Dans ce projet, l'ingestion est réalisée par un script Python.

**KPI (Key Performance Indicator)**
Indicateur clé de performance. Mesure quantifiable utilisée pour évaluer l'atteinte d'un objectif métier. Exemples : chiffre d'affaires, nombre de commandes, panier moyen.

**Mart**
Voir *Data Mart*.

**Modèle DBT**
Fichier SQL géré par DBT représentant une transformation de données. Chaque modèle correspond à une table ou une vue dans BigQuery.

**Pipeline**
Enchaînement automatisé d'étapes de traitement de données. Dans ce projet : ingestion → staging → marts → dashboard.

**Profil DBT (`profiles.yml`)**
Fichier de configuration DBT contenant les paramètres de connexion à l'entrepôt de données. Stocké dans `~/.dbt/` (hors du repo) pour protéger les credentials.

**Raw**
Couche de données brutes dans BigQuery. Les données y sont chargées telles quelles depuis les fichiers CSV, sans aucune transformation.

**Schéma en étoile**
Modèle de données dimensionnel composé d'une table de faits centrale reliée à plusieurs tables de dimension. Optimisé pour les requêtes analytiques.

**Service Account**
Compte technique GCP utilisé pour authentifier une application auprès des services Google Cloud (BigQuery). Les credentials sont fournis sous forme de fichier JSON.

**Staging**
Couche intermédiaire de données dans BigQuery. Les données y sont nettoyées, typées et renommées depuis la couche raw, sans agrégation.

**Streamlit**
Framework Python open source permettant de créer des applications web et des dashboards interactifs. Dans ce projet, Streamlit expose les KPIs depuis BigQuery.

---

## Termes métier

**Chiffre d'affaires (CA)**
Total des revenus générés par les ventes sur une période donnée. Calculé comme la somme des prix des articles commandés (`SUM(price)`).

**Dataset Olist**
Jeu de données public disponible sur Kaggle représentant l'activité réelle d'une marketplace e-commerce brésilienne. Il contient des données sur les commandes, clients, produits, vendeurs, paiements et avis clients.

**E-commerce**
Commerce électronique. Activité d'achat et de vente de produits ou services via internet.

**Marketplace**
Plateforme mettant en relation des vendeurs et des acheteurs. Olist est une marketplace brésilienne permettant à des petits commerçants de vendre leurs produits en ligne.

**Panier moyen**
Valeur moyenne d'une commande. Calculé comme le chiffre d'affaires divisé par le nombre de commandes (`CA / nombre de commandes`).

**Pipeline data**
Voir *Pipeline*.

**Plateforme analytique**
Système complet permettant de collecter, stocker, transformer et visualiser des données à des fins d'analyse et de prise de décision.
