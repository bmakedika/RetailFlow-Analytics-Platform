# imports

import streamlit as st
import pandas as pd
import os
import datetime
from dotenv import load_dotenv
from bigquery_client import run_query

# config

load_dotenv()

# UI header

st.title("Retailflow Dashboard")

# Sidebar filters

st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start date")
end_date = st.sidebar.date_input("End date")

if not start_date:
    start_date = datetime.date(2016, 1, 1)

if not end_date:
    end_date = datetime.date.today()

# Querying data from BigQuery

query_kpi = f"""
SELECT
    SUM(total_orders) AS total_orders,
    SUM(total_revenue) AS total_revenue,
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
WHERE order_date BETWEEN '{start_date}' AND '{end_date}'
"""

query_customers = f"""
SELECT
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM `retailflow-analytics.ecommerce_staging.dim_customers`
"""

query_time = f"""
SELECT
    order_date,
    total_orders,
    total_revenue
FROM `retailflow-analytics.ecommerce_staging.fct_orders`
WHERE order_date BETWEEN '{start_date}' AND '{end_date}'
ORDER BY order_date
"""

# Data extraction

df_kpi = run_query(query_kpi)
df_customers = run_query(query_customers)
df_time = run_query(query_time)

# KPI calculation

total_orders = int(df_kpi["total_orders"].fillna(0).iloc[0])
total_customers = int(df_customers["total_customers"].fillna(0).iloc[0])
total_revenue = round(float(df_kpi["total_revenue"].fillna(0).iloc[0]), 2)

# UI display

col1, col2, col3 = st.columns(3)

col1.metric("Orders", total_orders)
col2.metric("Customers", total_customers)
col3.metric("Revenue", total_revenue)

# Time series chart

st.markdown("### Orders & Revenue Over Time")

if not df_time.empty:
    st.line_chart(
        df_time.set_index("order_date")[["total_orders", "total_revenue"]]
    )
else:
    st.warning("No data available for selected period")
