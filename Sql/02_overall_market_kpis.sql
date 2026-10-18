SELECT
    COUNT(*) AS total_properties,
    COUNT(DISTINCT city) AS total_cities,
    COUNT(DISTINCT locality) AS total_localities,
    ROUND(AVG(price_inr), 2) AS avg_property_price,
    MIN(price_inr) AS min_property_price,
    MAX(price_inr) AS max_property_price,
    ROUND(AVG(area_sqft), 2) AS avg_area_sqft,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft
FROM `clever-tube-467215-u0.Real_Estate.properties`;