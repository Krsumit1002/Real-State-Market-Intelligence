SELECT
    property_id,
    city,
    locality,
    area_sqft,
    price_inr,
    price_per_sqft
FROM `clever-tube-467215-u0.Real_Estate.properties`
ORDER BY price_per_sqft DESC
LIMIT 10;