import subprocess
import sys

scripts = [
    "ingest.py",
    "load_to_bigquery.py",
]

for script in scripts:
    print(f"\nRunning {script}...")

    result = subprocess.run(
        [sys.executable, script],
        check=False
    )

    if result.returncode != 0:
        raise SystemExit(
            f"Pipeline failed at {script}"
        )

print("\nPipeline completed successfully!")