SELECT
    property_type,
    COUNT(*) AS total_properties,
    ROUND(AVG(area_sqft), 2) AS avg_area,
    ROUND(AVG(price_inr), 2) AS avg_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft
FROM `clever-tube-467215-u0.Real_Estate.properties`
GROUP BY property_type
ORDER BY avg_price DESC;