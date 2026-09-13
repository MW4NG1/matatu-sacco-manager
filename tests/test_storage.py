import os
import json
import pytest
from utils.storage import load_json, save_json

def test_save_and_load_json(tmp_path):
    """Test saving data to a JSON file and reading it back."""
    test_file = tmp_path / "test_sacco_data.json"
    sample_data = [
        {"id": 1, "route": "CBD - Westlands", "fare": 100},
        {"id": 2, "route": "CBD - Karen", "fare": 150}
    ]

    save_json(str(test_file), sample_data)
    assert os.path.exists(test_file)

    loaded_data = load_json(str(test_file))
    assert loaded_data == sample_data