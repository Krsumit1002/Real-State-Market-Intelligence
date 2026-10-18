WITH property_analysis AS (
    SELECT
        property_id,
        city,
        locality,
        area_sqft,
        price_inr,
        price_per_sqft,
        CASE
            WHEN price_inr < 5000000 THEN 'Budget'
            WHEN price_inr < 15000000 THEN 'Mid-Range'
            ELSE 'Premium'
        END AS price_category
    FROM `clever-tube-467215-u0.Real_Estate.properties`
)
SELECT
    price_category,
    COUNT(*) AS total_properties,
    ROUND(AVG(price_inr), 2) AS avg_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft,
    ROUND(AVG(area_sqft), 2) AS avg_area
FROM property_analysis
GROUP BY price_category
ORDER BY avg_price DESC;