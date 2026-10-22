# 🏠 Indian Real Estate Market Intelligence

An interactive **Power BI dashboard** designed to analyze Indian real estate listings, explore property prices, compare cities and localities, and understand property-type distributions using data analytics.

## 🔗 Live Dashboard

**[View Interactive Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZThiMGNkOTItODQ1YS00YTYyLThjODAtYzczZDAzZTk1ODkzIiwidCI6IjJkYzZkZDEwLTVhZGQtNDNhOC1iODNjLTJlYWJjMWFjYWQzZiJ9)**

Explore the interactive report by selecting cities, property types, localities, price ranges, and property area ranges.

## 📌 Project Overview

The Indian Real Estate Market Intelligence project focuses on transforming property listing data into meaningful insights through data preparation, SQL analysis, cloud data storage, and interactive visualization.

The project uses **Python, SQL, Google BigQuery, and Microsoft Power BI** to explore property prices, compare average prices across cities and localities, and analyze property characteristics through an interactive dashboard.

## 🎯 Project Objectives

- Analyze property prices across different Indian cities and localities.
- Compare average property prices by city and locality.
- Understand the distribution of different property types.
- Explore property price and area distributions.
- Build an interactive dashboard with dynamic filters.
- Demonstrate an end-to-end data analytics workflow.

## 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | Data preparation and cleaning |
| SQL | Data querying and analysis |
| Google BigQuery | Cloud data storage and querying |
| Microsoft Power BI | Dashboard development and visualization |
| Excel / CSV | Dataset handling, where applicable |

## 📂 Dataset

**Dataset:** [House Price Prediction Challenge – Kaggle](https://www.kaggle.com/datasets/anmolkumar/house-price-prediction-challenge)

- Approximate records: **29,451**
- BigQuery dataset: `Real_Estate`
- Tables used: `properties`, `properties_staging`

### Key Columns

| Column | Description |
|---|---|
| `property_id` | Unique property/listing identifier |
| `city` | City of the property |
| `locality` | Property locality |
| `property_type` | Property type or category |
| `area_sqft` | Property area in square feet |
| `price_inr` | Property price in Indian Rupees |
| `listing_date` | Property listing date field |
| `price_per_sqft` | Price per square foot |

**Data quality note:** The `listing_date` field appears to contain null values in the source data. Therefore, reliable time-based trend analysis is not claimed in this project.

## 📊 Dashboard Features

### 1. Key Performance Indicators (KPIs)

The dashboard provides a high-level overview through KPI cards:

- Total Properties
- Average Property Price
- Average Property Area
- Unique Localities

### 2. Interactive Filters

Users can dynamically filter the dashboard using:

- **City:** Focus on a selected city.
- **Property Type:** Analyze specific property categories.
- **Locality:** Explore individual localities.
- **Price Range:** Filter properties within a selected price range.
- **Area Range:** Filter properties by area in square feet.

### 3. Data Visualizations

- **Average Property Price by City:** Compare average property prices across cities.
- **Top 10 Localities by Average Property Price:** Identify localities with higher average listing prices.
- **Property Type Distribution:** Understand the distribution of property categories.
- **Property Price Distribution:** Explore how listed prices are distributed.
- **Property Size Analysis:** Examine relationships involving property area and price.
- **Property Price by City – Treemap:** Compare city-level property price measures visually.
- **Average Price Analysis – Matrix:** Review price measures across available categories.

## 🔄 Project Workflow

1. **Data Acquisition:** Obtained the real estate dataset from Kaggle.
2. **Data Preparation:** Used Python for data inspection and preparation.
3. **Cloud Data Storage:** Loaded data into Google BigQuery.
4. **SQL Analysis:** Queried property data to explore prices and related dimensions.
5. **Power BI Integration:** Connected the prepared data to Power BI.
6. **Dashboard Development:** Created KPI cards, slicers, and interactive visualizations.
7. **Report Publishing:** Published the dashboard online using Power BI.

## 💡 Key Skills Demonstrated

- Data cleaning and preparation
- SQL querying and analytical thinking
- Cloud data management with Google BigQuery
- Interactive dashboard development
- KPI design and data visualization
- Business-oriented data exploration
- Data storytelling and reporting

## 🚀 Future Enhancements

- Investigate missing listing dates and improve data quality.
- Add median property price and validated price-per-square-foot comparisons.
- Expand SQL analysis with additional business questions.
- Improve dashboard layout, accessibility, and mobile responsiveness.
- Add dashboard screenshots and SQL query documentation to the repository.

## 👨‍💻 Author

**Sumit Kumar**

- **GitHub:** [Krsumit1002](https://github.com/Krsumit1002)
- **LinkedIn:** [Sumit Kumar](https://www.linkedin.com/in/sumit-kumar-693337214/)
- **Live Project:** [Indian Real Estate Market Intelligence](https://app.powerbi.com/view?r=eyJrIjoiZThiMGNkOTItODQ1YS00YTYyLThjODAtYzczZDAzZTk1ODkzIiwidCI6IjJkYzZkZDEwLTVhZGQtNDNhOC1iODNjLTJlYWJjMWFjYWQzZiJ9)

---

*This project was developed as part of a data analytics portfolio to demonstrate practical skills in Python, SQL, Google BigQuery, and Power BI.*
