
from pathlib import Path
from google.cloud import bigquery

def validate_data(client, table_id):
    query = f"""
        SELECT
            COUNT(*) AS total_rows,
            COUNTIF(property_id IS NULL) AS missing_ids,
            COUNTIF(city IS NULL OR TRIM(city) = '') AS missing_cities,
            COUNTIF(area_sqft IS NULL OR area_sqft <= 0) AS invalid_areas,
            COUNTIF(price_inr IS NULL OR price_inr <= 0) AS invalid_prices
        FROM `{table_id}`
    """

    result = list(client.query(query).result())[0]

    print("\nData Quality Report")
    print("-------------------")
    print(f"Total rows: {result.total_rows}")
    print(f"Missing property IDs: {result.missing_ids}")
    print(f"Missing cities: {result.missing_cities}")
    print(f"Invalid areas: {result.invalid_areas}")
    print(f"Invalid prices: {result.invalid_prices}")

    if (
        result.missing_ids > 0
        or result.missing_cities > 0
        or result.invalid_areas > 0
        or result.invalid_prices > 0
    ):
        raise ValueError("Data quality validation failed!")

    print("Data quality validation passed!")

# 1. Google Cloud project aur dataset
PROJECT_ID = "clever-tube-467215-u0"
DATASET_ID = "Real_Estate"
TABLE_ID = "properties"

# 2. CSV file ka path
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "Data" / "properties_clean.csv"

# 3. BigQuery client
client = bigquery.Client(project=PROJECT_ID)

# 4. Target table
table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# 5. CSV ko BigQuery mein load karna
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

with open(CSV_PATH, "rb") as csv_file:
    job = client.load_table_from_file(
        csv_file,
        table_id,
        job_config=job_config,
    )

job.result()

# 6. Confirm karna
table = client.get_table(table_id)

print("Data successfully loaded into BigQuery!")
print(f"Table: {table.full_table_id}")
print(f"Rows loaded: {table.num_rows}")
print(f"Columns: {len(table.schema)}")

validate_data(client, table_id)
