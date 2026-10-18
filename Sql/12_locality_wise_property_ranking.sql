SELECT
    property_id,
    city,
    locality,
    price_inr,
    RANK() OVER (
        PARTITION BY city
        ORDER BY price_inr DESC
    ) AS price_rank
FROM `clever-tube-467215-u0.Real_Estate.properties`
ORDER BY city, price_rank;