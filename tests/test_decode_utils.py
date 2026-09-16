import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.decode_utils import DecodeUtils


def test_decode_inspect():
    decoded = ["json-data", "yaml-data", "xml-data"]
    report = DecodeUtils.inspect(decoded)
    assert report.decoded == ["json-data", "yaml-data", "xml-data"]
    assert report.timestamp
