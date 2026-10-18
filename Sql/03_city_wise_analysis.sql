SELECT
    city,
    COUNT(*) AS total_properties,
    ROUND(AVG(price_inr), 2) AS avg_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft,
    MIN(price_inr) AS lowest_price,
    MAX(price_inr) AS highest_price
FROM `clever-tube-467215-u0.Real_Estate.properties`
GROUP BY city
ORDER BY avg_price DESC;