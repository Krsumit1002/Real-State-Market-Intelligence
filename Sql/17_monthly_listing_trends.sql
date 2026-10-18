SELECT
    EXTRACT(YEAR FROM listing_date) AS listing_year,
    EXTRACT(MONTH FROM listing_date) AS listing_month,
    COUNT(*) AS total_listings,
    ROUND(AVG(price_inr), 2) AS avg_price,
    ROUND(AVG(price_per_sqft), 2) AS avg_price_per_sqft
FROM `clever-tube-467215-u0.Real_Estate.properties`
GROUP BY listing_year, listing_month
ORDER BY listing_year, listing_month;