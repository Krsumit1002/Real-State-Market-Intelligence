
# Real Estate Market Intelligence Pipeline

An end-to-end data engineering and analytics project focused on
real estate property data across Noida and Gurugram.

## Current Features

- Python-based CSV ingestion
- Duplicate property ID handling
- Data validation and rejection of invalid records
- Price per square foot calculation
- Separate clean and rejected CSV outputs

## Tech Stack

- Python
- Pandas
- CSV
- Git and GitHub

## Project Structure

```text
Real-State-Market-Intelligence/
├── Data/
│   ├── properties.csv
│   ├── properties_clean.csv
│   └── properties_rejected.csv
├── ingest.py
└── README.md
```

## How to Run

1. Install Python.
2. Install Pandas:

   ```bash
   python -m pip install pandas
   ```

3. Run the ingestion script:

   ```bash
   python ingest.py
   ```

## Next Development Goals

- Load cleaned data into Google BigQuery
- Build SQL transformations using dbt
- Automate the pipeline with Apache Airflow
- Create a real estate analytics dashboard

## Data Disclaimer

The current CSV data is synthetic sample data for development
and testing. It does not represent verified live property listings.
