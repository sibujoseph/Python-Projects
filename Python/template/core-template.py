import logging
from pathlib import Path
from typing import Dict, Any


logger = logging.getLogger(__name__)


def run_job(config: Dict[str, Any]) -> None:
    """
    Main business logic.
    """
    logger.info("Job started")

    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "results.txt"
    with open(file_path, "w") as f:
        f.write("Hello, Production!\n")

    logger.info(f"Results written to {file_path}")
    logger.info("Job completed successfully")
