WITH comparison AS (
    SELECT
        property_id,
        city,
        locality,
        price_per_sqft,
        AVG(price_per_sqft) OVER (
            PARTITION BY city
        ) AS city_avg_rate
    FROM `clever-tube-467215-u0.Real_Estate.properties`
)
SELECT
    property_id,
    city,
    locality,
    ROUND(price_per_sqft, 2) AS property_rate,
    ROUND(city_avg_rate, 2) AS city_avg_rate,
    ROUND(price_per_sqft - city_avg_rate, 2) AS rate_difference,
    CASE
        WHEN price_per_sqft > city_avg_rate THEN 'Above Average'
        WHEN price_per_sqft < city_avg_rate THEN 'Below Average'
        ELSE 'Equal to Average'
    END AS price_position
FROM comparison
ORDER BY city, rate_difference DESC;