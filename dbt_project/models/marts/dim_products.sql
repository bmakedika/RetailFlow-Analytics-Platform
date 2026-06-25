SELECT
    product_id,
    product_category,
    product_name_length,
    product_description_length

FROM {{ ref('stg_products') }}
