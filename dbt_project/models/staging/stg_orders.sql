SELECT
    order_id,
    customer_id,
    order_status,
    CAST(order_purchase_timestamp AS TIMESTAMP) AS purchase_ts,
    CAST(order_delivered_customer_date AS TIMESTAMP) AS delivered_ts,

FROM `retailflow-analytics.ecommerce_raw.orders`
