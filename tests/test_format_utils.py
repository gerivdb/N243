import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.format_utils import FormatUtils


def test_format_inspect():
    formats = ["json", "yaml", "xml"]
    report = FormatUtils.inspect(formats)
    assert report.formats == ["json", "yaml", "xml"]
    assert report.timestamp
