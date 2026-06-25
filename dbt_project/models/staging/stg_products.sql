SELECT
    product_id,
    CAST(product_category_name AS STRING) AS product_category,
    CAST(product_name_lenght AS FLOAT64) AS product_name_length,
    CAST(product_description_lenght AS FLOAT64) AS product_description_length,
    CAST(product_photos_qty AS FLOAT64) AS product_photos_quantity,
    CAST(product_weight_g AS FLOAT64) AS product_weight,
    CAST(product_length_cm AS FLOAT64) AS product_length,
    CAST(product_height_cm AS FLOAT64) AS product_height,
    CAST(product_width_cm AS FLOAT64) AS product_width

FROM `retailflow-analytics.ecommerce_raw.products`