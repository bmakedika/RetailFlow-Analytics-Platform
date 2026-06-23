import pandas as pd
from google.cloud import bigquery

def read_csv(file_path):
    return pd.read_csv(file_path)

def load_to_bigquery(client, df, table_id, job_config):
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

def process_table(client, project_id, dataset, table, file_name, job_config, logger):
    try:
        logger.info(f"Traitement en cours : {table}")
        
        file_path = f"data/raw/{file_name}"
        df = pd.read_csv(file_path)
        
        table_id = f"{project_id}.{dataset}.{table}"

        job = client.load_table_from_dataframe(df, table_id, job_config=job_config) 
        job.result()

        logger.info(f"{table} chargée avec succès\n")
        return None

    except Exception as e:
        logger.error(f"Erreur lors du traitement {table}: {str(e)}\n")
        return (table, str(e))
