import pandas as pd
from google.cloud import bigquery

client = bigquery.Client()

data_src = {
    "orders": "olist_orders_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "order_items": "olist_order_items_dataset.csv"
}

project_id = "retailflow-analytics"
dataset = "ecommerce_raw"

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
) 

error_tables = []

for table, file_name in data_src.items():
    print(f"Traitement en cours {table}...")

    try:
        file_path = f"data/raw/{file_name}"
        df = pd.read_csv(file_path)

        table_id = f"{project_id}.{dataset}.{table}"

        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()

        print(f"{table} chargement réussi\n")
    
    except Exception as e:
        print(f"Erreur lors du chargement de {table}: {str(e)}\n")
        error_tables.append((table, str(e)))
        continue

print("\nPipeline d'exécution terminée")

if error_tables:
    print("\nErreurs détectées:")
    for table, error in error_tables:
        print(f" - {table}: {error}")
    
else:
    print("Toutes les tables ont été chargées avec succès !")