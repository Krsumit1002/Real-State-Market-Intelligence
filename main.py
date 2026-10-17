
import subprocess
import sys
import logging
from pathlib import Path

# Logs terminal mein show honge
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

BASE_DIR = Path(__file__).resolve().parent

SCRIPTS = [
    "ingest.py",
    "load_to_bigquery.py",
]

def run_pipeline():
    logging.info("Real Estate Pipeline started")

    for script in SCRIPTS:
        script_path = BASE_DIR / script

        if not script_path.exists():
            raise FileNotFoundError(
                f"Required script not found: {script}"
            )

        logging.info("Running %s", script)

        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=BASE_DIR,
            check=False,
        )

        if result.returncode != 0:
            logging.error(
                "Pipeline failed at %s", script
            )
            raise SystemExit(result.returncode)

        logging.info("%s completed successfully", script)

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
