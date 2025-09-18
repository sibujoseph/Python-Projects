#!/usr/bin/env python3
"""
Template for a comprehensive Python program.

Features:
- Entry point with __main__
- CLI arguments (argparse)
- Config loading (JSON/YAML/env)
- Logging setup
- Main business logic
- Error handling
- Unit testing hook
"""

import os
import sys
import argparse
import logging
import json
from pathlib import Path
from typing import Any, Dict, Optional

# =============================
# Configuration Management
# =============================

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Load configuration from JSON file, or provide defaults.
    """
    default_config = {
        "debug": False,
        "log_level": "INFO",
        "output_dir": "output"
    }

    if config_path and Path(config_path).exists():
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
            return {**default_config, **user_config}
        except Exception as e:
            logging.error(f"Failed to load config {config_path}: {e}")
            return default_config
    else:
        return default_config


# =============================
# Logging Setup
# =============================

def setup_logging(level: str = "INFO") -> None:
    """
    Configure logging.
    """
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )


# =============================
# Core Logic
# =============================

def main_logic(config: Dict[str, Any]) -> None:
    """
    Main business logic goes here.
    """
    logging.info("Starting main logic...")
    
    # Example logic
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    sample_file = output_dir / "sample_output.txt"
    with open(sample_file, "w") as f:
        f.write("Hello, World!\n")

    logging.info(f"Output written to {sample_file}")
    logging.info("Main logic completed successfully.")


# =============================
# CLI Argument Parsing
# =============================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Comprehensive Python Program Template")
    parser.add_argument(
        "-c", "--config", type=str, help="Path to config file (JSON)"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug mode"
    )
    return parser.parse_args()


# =============================
# Entry Point
# =============================

def main():
    args = parse_args()

    # Load configuration
    config = load_config(args.config)

    # Override debug flag from CLI
    if args.debug:
        config["debug"] = True
        config["log_level"] = "DEBUG"

    # Setup logging
    setup_logging(config.get("log_level", "INFO"))

    logging.debug(f"Configuration: {config}")

    try:
        main_logic(config)
    except Exception as e:
        logging.exception(f"Unhandled exception: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


# =============================
# Unit Testing Hook
# =============================

def test_sample():
    """
    Example test function.
    Use pytest or unittest for real tests.
    """
    cfg = {"output_dir": "test_output"}
    setup_logging("DEBUG")
    main_logic(cfg)
    assert Path("test_output/sample_output.txt").exists()
