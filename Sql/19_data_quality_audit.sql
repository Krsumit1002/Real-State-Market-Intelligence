SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT property_id) AS unique_property_ids,
    COUNTIF(property_id IS NULL) AS missing_ids,
    COUNTIF(city IS NULL OR TRIM(city) = '') AS missing_cities,
    COUNTIF(locality IS NULL OR TRIM(locality) = '') AS missing_localities,
    COUNTIF(area_sqft IS NULL OR area_sqft <= 0) AS invalid_areas,
    COUNTIF(price_inr IS NULL OR price_inr <= 0) AS invalid_prices,
    COUNTIF(listing_date IS NULL) AS missing_listing_dates
FROM `clever-tube-467215-u0.Real_Estate.properties`;