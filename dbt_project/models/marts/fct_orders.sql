SELECT
    DATE(o.purchase_ts) AS order_date,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(i.price) AS total_revenue

FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} i
ON o.order_id = i.order_id

GROUP BY order_date
