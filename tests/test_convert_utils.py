import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.convert_utils import ConvertUtils


def test_convert_inspect():
    conversions = ["conv-1", "conv-2", "conv-3"]
    report = ConvertUtils.inspect(conversions)
    assert report.conversions == ["conv-1", "conv-2", "conv-3"]
    assert report.timestamp
