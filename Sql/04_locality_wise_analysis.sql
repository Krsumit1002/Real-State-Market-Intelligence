SELECT
    city,
    locality,
    COUNT(*) AS total_properties,
    ROUND(AVG(price_inr), 2) AS avg_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft,
    RANK() OVER (
        PARTITION BY city
        ORDER BY AVG(price_per_sqft) DESC
    ) AS locality_rank
FROM `clever-tube-467215-u0.Real_Estate.properties`
GROUP BY city, locality
ORDER BY city, locality_rank;