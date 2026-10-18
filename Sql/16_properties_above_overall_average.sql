SELECT
    property_id,
    city,
    locality,
    price_inr
FROM `clever-tube-467215-u0.Real_Estate.properties`
WHERE price_inr > (
    SELECT AVG(price_inr)
    FROM `clever-tube-467215-u0.Real_Estate.properties`
)
ORDER BY price_inr DESC;