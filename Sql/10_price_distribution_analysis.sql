SELECT
    CASE
        WHEN price_inr < 5000000 THEN 'Under 50 Lakh'
        WHEN price_inr < 10000000 THEN '50 Lakh - 1 Crore'
        WHEN price_inr < 20000000 THEN '1 - 2 Crore'
        ELSE 'Above 2 Crore'
    END AS price_range,

    COUNT(*) AS total_properties,
    ROUND(AVG(price_inr), 2) AS avg_price,
    MIN(price_inr) AS min_price,
    MAX(price_inr) AS max_price

FROM `clever-tube-467215-u0.Real_Estate.properties`

GROUP BY price_range
ORDER BY MIN(price_inr);