from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig

from ingestion.config import PROJECT_ID, DATASET, DATA_SOURCES
from ingestion.pipeline import process_table
from ingestion.logger import setup_logger

logger = setup_logger()

client = bigquery.Client()

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
) 

errors = []

logger.info("Démarrage du pipeline d'ingestion...\n")

for table, file_name in DATA_SOURCES.items():

    error = process_table(
        client,
        PROJECT_ID,
        DATASET,
        table,
        file_name,
        job_config,
        logger
    )

    if error:
        errors.append(error)

logger.info("Exécution du pipeline terminée")

if errors:
    logger.warning("Erreurs détectées:")
    for table, error in errors:
        logger.warning(f" - {table}: {error}")
    
else:
    logger.info("Toutes les tables ont été chargées avec succès !")