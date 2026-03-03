import os
import json


OUTPUT_PATH = "/app/output.json"


def test_output_file_exists():
    """Check that output.json file is created."""
    assert os.path.exists(OUTPUT_PATH), "output.json was not created"


def test_output_is_valid_json():
    """Check that output.json contains valid JSON."""
    with open(OUTPUT_PATH) as f:
        data = json.load(f)
    assert isinstance(data, dict), "Output is not a valid JSON object"


def test_status_is_success():
    """Check that status field equals 'success'."""
    with open(OUTPUT_PATH) as f:
        data = json.load(f)
    assert "status" in data, "Missing 'status' key"
    assert data["status"] == "success", "Status is not 'success'"


def test_processed_flag():
    """Check that processed flag is True."""
    with open(OUTPUT_PATH) as f:
        data = json.load(f)
    assert "processed" in data, "Missing 'processed' key"
    assert data["processed"] is True, "Processed flag is not True"