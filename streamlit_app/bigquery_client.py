from google.cloud import bigquery
import streamlit as st


@st.cache_resource
def get_client():
    return bigquery.Client()


@st.cache_data
def run_query(query: str):
    client = get_client()
    return client.query(query).to_dataframe()
