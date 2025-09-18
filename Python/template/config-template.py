import json
import os
from pathlib import Path
from typing import Any, Dict


DEFAULT_CONFIG = {
    "debug": False,
    "log_level": "INFO",
    "output_dir": "output"
}


def load_config(config_path: str | None = None) -> Dict[str, Any]:
    """
    Load JSON config file and merge with defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if config_path:
        path = Path(config_path)
        if path.exists():
            try:
                with open(path, "r") as f:
                    user_config = json.load(f)
                config.update(user_config)
            except Exception as e:
                raise RuntimeError(f"Error reading config {config_path}: {e}")
        else:
            raise FileNotFoundError(f"Config file not found: {config_path}")

    return config
