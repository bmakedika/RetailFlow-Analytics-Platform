SELECT
    customer_id,
    unique_id,
    city,
    state

FROM {{ ref('stg_customers') }}
