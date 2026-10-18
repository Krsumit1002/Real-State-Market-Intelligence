SELECT
    property_id,
    city,
    locality,
    property_type,
    area_sqft,
    price_inr,
    price_per_sqft,

    RANK() OVER (
        PARTITION BY city
        ORDER BY price_inr DESC
    ) AS price_rank

FROM `clever-tube-467215-u0.Real_Estate.properties`

ORDER BY city, price_rank;