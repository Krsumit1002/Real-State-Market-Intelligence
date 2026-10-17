
from pathlib import Path
from google.cloud import bigquery

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
