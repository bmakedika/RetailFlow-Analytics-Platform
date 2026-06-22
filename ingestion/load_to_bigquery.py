from google.cloud import bigquery
from ingestion.config import PROJECT_ID, DATASET, DATA_SOURCES
from ingestion.pipeline import process_table
from google.cloud.bigquery import LoadJobConfig

client = bigquery.Client()

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
) 

errors = []

print("Démarrage du pipeline d'ingestion...\n")

for table, file_name in DATA_SOURCES.items():

    error = process_table(
        client,
        PROJECT_ID,
        DATASET,
        table,
        file_name,
        job_config
    )

    if error:
        errors.append(error)

print("\nExécution du pipeline terminée")

if errors:
    print("\nErreurs détectées:")
    for table, error in errors:
        print(f" - {table}: {error}")
    
else:
    print("Toutes les tables ont été chargées avec succès !")