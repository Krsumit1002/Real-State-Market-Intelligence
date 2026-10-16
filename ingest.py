
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "properties.csv"
OUTPUT_FILE = BASE_DIR / "data" / "properties_clean.csv"
REJECTED_FILE = BASE_DIR / "data" / "properties_rejected.csv"


def main():
    print("Starting data ingestion...")

    # Read the CSV file
    df = pd.read_csv(INPUT_FILE)
    print(f"Rows loaded: {len(df)}")

    # Remove duplicate property IDs
    before = len(df)
    df = df.drop_duplicates(subset=["property_id"])
    print(f"Duplicates removed: {before - len(df)}")

    # Convert columns to the correct data types
    df["area_sqft"] = pd.to_numeric(
        df["area_sqft"], errors="coerce"
    )
    df["price_inr"] = pd.to_numeric(
        df["price_inr"], errors="coerce"
    )
    df["listing_date"] = pd.to_datetime(
        df["listing_date"], errors="coerce"
    )

    # Identify invalid records
    valid = (
        df["property_id"].notna()
        & df["city"].notna()
        & df["locality"].notna()
        & df["area_sqft"].gt(0)
        & df["price_inr"].gt(0)
        & df["listing_date"].notna()
    )

    clean_df = df.loc[valid].copy()
    rejected_df = df.loc[~valid].copy()

    # Calculate price per square foot
    clean_df["price_per_sqft"] = (
        clean_df["price_inr"] / clean_df["area_sqft"]
    ).round(2)

    # Save the results
    clean_df.to_csv(OUTPUT_FILE, index=False)
    rejected_df.to_csv(REJECTED_FILE, index=False)

    print(f"Valid rows: {len(clean_df)}")
    print(f"Rejected rows: {len(rejected_df)}")
    print("Ingestion completed successfully!")


if __name__ == "__main__":
    main()

