SELECT
    city,
    COUNT(*) AS total_properties,
    ROUND(AVG(price_inr), 2) AS avg_property_price,
    MIN(price_inr) AS min_property_price,
    MAX(price_inr) AS max_property_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft
FROM `clever-tube-467215-u0.Real_Estate.properties`
GROUP BY city
ORDER BY avg_property_price DESC;