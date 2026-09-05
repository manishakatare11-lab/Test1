import json
import os
from pathlib import Path

def read_json(json_file_path: str):
    # directory of the project root (adjust parents if needed)
    base_dir = Path(__file__).resolve().parents[1]

    file_path = (base_dir / json_file_path).resolve()

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)