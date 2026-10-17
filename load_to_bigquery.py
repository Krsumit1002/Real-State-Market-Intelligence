
from pathlib import Path
from google.cloud import bigquery

PROJECT_ID = "clever-tube-467215-u0"
DATASET_ID = "Real_Estate"
TABLE_ID = "properties"
STAGING_TABLE_ID = "properties_staging"

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "Data" / "properties_clean.csv"

client = bigquery.Client(project=PROJECT_ID)

table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
staging_table_id = (
    f"{PROJECT_ID}.{DATASET_ID}.{STAGING_TABLE_ID}"
)


def validate_data(client, target_table_id):
    query = f"""
        SELECT
            COUNT(*) AS total_rows,
            COUNTIF(property_id IS NULL) AS missing_ids,
            COUNTIF(city IS NULL OR TRIM(city) = '') AS missing_cities,
            COUNTIF(area_sqft IS NULL OR area_sqft <= 0) AS invalid_areas,
            COUNTIF(price_inr IS NULL OR price_inr <= 0) AS invalid_prices
        FROM `{target_table_id}`
    """

    result = list(client.query(query).result())[0]

    print("\nData Quality Report")
    print("-------------------")
    print(f"Total rows: {result.total_rows}")
    print(f"Missing property IDs: {result.missing_ids}")
    print(f"Missing cities: {result.missing_cities}")
    print(f"Invalid areas: {result.invalid_areas}")
    print(f"Invalid prices: {result.invalid_prices}")

    if result.total_rows == 0:
        raise ValueError("Staging table is empty!")

    if (
        result.missing_ids > 0
        or result.missing_cities > 0
        or result.invalid_areas > 0
        or result.invalid_prices > 0
    ):
        raise ValueError("Data quality validation failed!")

    print("Data quality validation passed!")


# Step 1: CSV ko staging table mein load karo
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

print("Loading CSV into staging table...")

with open(CSV_PATH, "rb") as csv_file:
    job = client.load_table_from_file(
        csv_file,
        staging_table_id,
        job_config=job_config,
    )

job.result()

print("Staging table loaded successfully.")

# Step 2: Staging data validate karo
validate_data(client, staging_table_id)

# Step 3: Validation pass hone par final table replace karo
copy_config = bigquery.CopyJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

print("\nUpdating final properties table...")

copy_job = client.copy_table(
    staging_table_id,
    table_id,
    job_config=copy_config,
)

copy_job.result()

# Step 4: Final table confirm karo
table = client.get_table(table_id)

print("\nFinal table updated successfully!")
print(f"Table: {table.full_table_id}")
print(f"Rows loaded: {table.num_rows}")
print(f"Columns: {len(table.schema)}")
