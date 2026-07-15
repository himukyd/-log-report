import json
from pathlib import Path

def load_report():
    return json.loads(Path("/app/report.json").read_text())

def test_report_exists():
    """Success Criterion 1: report.json is created."""
    assert Path("/app/report.json").exists()

def test_report_values():
    """Success Criterion 2: report.json contains the correct summary."""
    report = load_report()

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"