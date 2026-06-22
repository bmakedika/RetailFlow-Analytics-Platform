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

for table, file_name in data_src.items():
    print(f"Traitement en cours {table}...")

    file_path = f"data/raw/{file_name}"
    df = pd.read_csv(file_path)

    table_id = f"{project_id}.{dataset}.{table}"

    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()

    print(f"{table} chargement réussi")
    
print("Toutes les tables sont chargées !")
