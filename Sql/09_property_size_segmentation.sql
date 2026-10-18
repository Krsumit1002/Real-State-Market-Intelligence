WITH size_analysis AS (
    SELECT
        property_id,
        area_sqft,
        price_inr,
        price_per_sqft,
        CASE
            WHEN area_sqft < 800 THEN 'Small'
            WHEN area_sqft < 1500 THEN 'Medium'
            ELSE 'Large'
        END AS size_category
    FROM `clever-tube-467215-u0.Real_Estate.properties`
)
SELECT
    size_category,
    COUNT(*) AS total_properties,
    ROUND(AVG(area_sqft), 2) AS avg_area,
    ROUND(AVG(price_inr), 2) AS avg_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft
FROM size_analysis
GROUP BY size_category
ORDER BY avg_area;