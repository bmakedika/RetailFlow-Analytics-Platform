import pandas as pd
from google.cloud import bigquery

client = bigquery.Client()

df = pd.read_csv("data/raw/olist_orders_dataset.csv")

table_id = "retailflow-analytics.ecommerce_raw.orders"

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
)

job = client.load_table_from_dataframe(df, table_id, job_config=job_config)

job.result()

print("Données importées dans BigQuery")