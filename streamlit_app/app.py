import streamlit as st
import pandas as pd
import os
import datetime
from google.cloud import bigquery
from dotenv import load_dotenv


load_dotenv()

client = bigquery.Client()

st.title("Retailflow Dashboard")

st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start date")
end_date = st.sidebar.date_input("End date")

if not start_date:
    start_date = datetime.date(2016, 1, 1)

if not end_date:
    end_date = datetime.date.today()


query_kpi = f"""
SELECT
    SUM(total_orders) AS total_orders,
    SUM(total_revenue) AS total_revenue,
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
WHERE order_date BETWEEN '{start_date}' AND '{end_date}'
"""

df_kpi = client.query(query_kpi).to_dataframe()


query_customers = f"""
SELECT
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM `retailflow-analytics.ecommerce_staging.dim_customers`
"""

df_customers = client.query(query_customers).to_dataframe()


query_kpi = f"""
SELECT
    SUM(total_orders) AS total_orders,
    SUM(total_revenue) AS total_revenue,
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
WHERE order_date BETWEEN '{start_date}' AND '{end_date}'
"""

df_kpi = client.query(query_kpi).to_dataframe()


query_customers = f"""
SELECT
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM `retailflow-analytics.ecommerce_staging.dim_customers`
"""

df_customers = client.query(query_customers).to_dataframe()



total_orders = int(df_kpi["total_orders"].fillna(0).iloc[0])
total_customers = int(df_customers["total_customers"].fillna(0).iloc[0])
total_revenue = round(float(df_kpi["total_revenue"].fillna(0).iloc[0]), 2)



col1, col2, col3 = st.columns(3)

col1.metric("Orders", int(total_orders))
col2.metric("Customers", int(total_customers))
col3.metric("Revenue", round(total_revenue, 2))


query_time = f"""
SELECT
    order_date,
    total_orders,
    total_revenue
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
WHERE order_date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY order_date
"""

df_time = client.query(query_time).to_dataframe()



st.markdown("### Orders & Revenue Over Time")

if not df_time.empty:
    st.line_chart(
        df_time.set_index("order_date")[["total_orders", "total_revenue"]]
    )
else:
    st.warning("No data available for selected period")
