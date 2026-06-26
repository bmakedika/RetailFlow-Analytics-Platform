SELECT
    order_id,
    CAST(product_id AS STRING) AS product_id,
    CAST(seller_id AS STRING) AS seller_id,
    CAST(price AS FLOAT64) AS price,
    CAST(freight_value AS FLOAT64) AS freight_value

FROM `retailflow-analytics.ecommerce_raw.order_items`
