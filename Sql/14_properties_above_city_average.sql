WITH city_comparison AS (
    SELECT
        property_id,
        city,
        locality,
        price_inr,
        AVG(price_inr) OVER (
            PARTITION BY city
        ) AS city_avg_price
    FROM `clever-tube-467215-u0.Real_Estate.properties`
)
SELECT
    property_id,
    city,
    locality,
    price_inr,
    ROUND(city_avg_price, 2) AS city_avg_price
FROM city_comparison
WHERE price_inr > city_avg_price
ORDER BY city, price_inr DESC;