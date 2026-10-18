SELECT
    property_id,
    city,
    locality,
    property_type,
    listing_date,
    area_sqft,
    price_inr
FROM `clever-tube-467215-u0.Real_Estate.properties`
ORDER BY listing_date DESC
LIMIT 10;