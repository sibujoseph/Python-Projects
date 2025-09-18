import sys
import logging
from my_project.cli import parse_args
from my_project.config import load_config
from my_project.logger import setup_logging
from my_project.core import run_job


def main():
    args = parse_args()
    config = load_config(args.config)

    if args.debug:
        config["debug"] = True
        config["log_level"] = "DEBUG"

    setup_logging(config["log_level"])
    logger = logging.getLogger(__name__)

    logger.debug(f"Loaded configuration: {config}")

    try:
        run_job(config)
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
