import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.parse_utils import ParseUtils


def test_parse_inspect():
    parsed = ["token-1", "token-2", "token-3"]
    report = ParseUtils.inspect(parsed)
    assert report.parsed == ["token-1", "token-2", "token-3"]
    assert report.timestamp
