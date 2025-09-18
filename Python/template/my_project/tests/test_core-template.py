import os
from pathlib import Path
from my_project.core import run_job


def test_run_job(tmp_path):
    config = {"output_dir": tmp_path}
    run_job(config)

    file_path = tmp_path / "results.txt"
    assert file_path.exists()
    assert "Hello" in file_path.read_text()
