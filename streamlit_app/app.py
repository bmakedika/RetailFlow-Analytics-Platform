import streamlit as st
import pandas as pd
import os

from google.cloud import bigquery
from dotenv import load_dotenv


load_dotenv()

client = bigquery.Client()

st.title("Retailflow Dashboard")

query = """
SELECT
    COUNT(*) AS total_orders
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
"""

df = client.query(query).to_dataframe()

st.metric("Total Orders", df["total_orders"][0])

query_time = """
SELECT
    order_date,
    total_orders
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
ORDER BY order_date
"""

df_time = client.query(query_time).to_dataframe()

st.line_chart(df_time.set_index("order_date"))


query_customers = """
SELECT
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM `retailflow-analytics.ecommerce_staging.dim_customers`
"""


df_customers = client.query(query_customers).to_dataframe()

st.metric("Total Customers", df_customers["total_customers"][0])
