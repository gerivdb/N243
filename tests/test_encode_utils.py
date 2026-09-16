import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.encode_utils import EncodeUtils


def test_encode_inspect():
    encoded = ["utf-8", "base64", "hex"]
    report = EncodeUtils.inspect(encoded)
    assert report.encoded == ["utf-8", "base64", "hex"]
    assert report.timestamp
