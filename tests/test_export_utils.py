import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.export_utils import ExportUtils


def test_export_inspect():
    exports = ["export-1", "export-2", "export-3"]
    report = ExportUtils.inspect(exports)
    assert report.exports == ["export-1", "export-2", "export-3"]
    assert report.timestamp
