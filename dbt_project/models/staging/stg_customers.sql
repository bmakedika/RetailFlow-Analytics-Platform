SELECT
    customer_id,
    CAST(customer_unique_id AS STRING) AS unique_id,
    CAST(customer_zip_code_prefix AS STRING) AS zip_code,
    CAST(customer_city AS STRING) AS city,
    CAST(customer_state AS STRING) AS state

FROM `retailflow-analytics.ecommerce_raw.customers`