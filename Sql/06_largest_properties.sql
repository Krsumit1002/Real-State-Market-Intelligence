SELECT
    property_id,
    city,
    locality,
    property_type,
    area_sqft,
    price_inr
FROM `clever-tube-467215-u0.Real_Estate.properties`
ORDER BY area_sqft DESC
LIMIT 10;