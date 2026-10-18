# Real Estate Market Intelligence Pipeline

A data analytics project that processes real estate property data using Python and Google BigQuery to analyze property prices, city-wise trends, property rankings, and market distribution.

## Project Overview

This project demonstrates an end-to-end data analytics workflow, from data ingestion and cleaning to cloud data storage and SQL-based analysis.

The pipeline validates property records, separates rejected data, calculates price per square foot, and loads validated records into BigQuery for analysis.

## Tech Stack

- **Python** — Data ingestion, cleaning, validation, and pipeline orchestration
- **Pandas** — Data manipulation and processing
- **Google BigQuery** — Cloud data warehouse and SQL analytics
- **SQL** — Aggregations, CTEs, CASE statements, window functions, and data quality checks
- **Git & GitHub** — Version control and project documentation

## Project Structure

```text
Real-Estate-Market-Intelligence/
│
├── Data/
│   ├── properties.csv
│   ├── properties_clean.csv
│   └── properties_rejected.csv
│
├── sql/
│   ├── 01_city_analysis.sql
│   ├── 02_overall_market_kpis.sql
│   ├── 03_city_wise_analysis.sql
│   ├── 04_locality_wise_analysis.sql
│   ├── 05_property_type_analysis.sql
│   ├── 06_largest_properties.sql
│   ├── 07_highest_price_per_sqft.sql
│   ├── 08_property_price_categories.sql
│   ├── 09_property_size_segmentation.sql
│   ├── 10_price_distribution_analysis.sql
│   ├── 11_city_wise_property_ranking.sql
│   ├── 12_locality_wise_property_ranking.sql
│   ├── 13_top_properties_by_city.sql
│   ├── 14_properties_above_city_average.sql
│   ├── 15_price_per_sqft_vs_city_average.sql
│   ├── 16_properties_above_overall_average.sql
│   ├── 17_monthly_listing_trends.sql
│   ├── 18_latest_property_listings.sql
│   ├── 19_data_quality_audit.sql
│   └── 20_dashboard_kpi_summary.sql
│
├── ingest.py
├── load_to_bigquery.py
├── main.py
├── .gitignore
└── README.md
```

## Data Pipeline

1. **Data ingestion:** Read raw property data from CSV.
2. **Data cleaning:** Remove duplicate property IDs and validate required fields.
3. **Data validation:** Check property area, price, and listing dates.
4. **Data enrichment:** Calculate price per square foot.
5. **Data separation:** Export valid records and rejected records into separate CSV files.
6. **BigQuery staging:** Load cleaned data into a staging table.
7. **Quality checks:** Validate the staged data before updating the final table.
8. **SQL analytics:** Analyze the processed data using SQL queries.

## SQL Analysis

The `sql/` directory contains 20 query files organized around the following analytical areas:

- Overall market KPIs
- City-wise and locality-wise property analysis
- Property type distribution
- Largest properties and price per square foot
- Price categories and property size segmentation
- Price distribution analysis
- City-wise and locality-wise property rankings
- Properties priced above city and overall averages
- Monthly listing trends and latest listings
- Data quality audits
- Dashboard KPI summaries

SQL techniques include `GROUP BY`, aggregate functions, `CASE WHEN`, Common Table Expressions (CTEs), and window functions such as `RANK()` and `ROW_NUMBER()`.

## BigQuery Configuration

- **Project ID:** `clever-tube-467215-u0`
- **Dataset:** `Real_Estate`
- **Staging table:** `properties_staging`
- **Final table:** `properties`

[Open Google BigQuery Console](https://console.cloud.google.com/bigquery?project=clever-tube-467215-u0)

## How to Run the Project

### Prerequisites

- Python 3.x
- Google Cloud project with BigQuery enabled
- Google Cloud authentication configured for the BigQuery client library

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

Install the required libraries used by the Python scripts, including:

```bash
pip install
