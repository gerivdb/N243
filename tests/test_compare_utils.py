import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.compare_utils import CompareUtils


def test_compare_inspect():
    comparisons = ["cmp-1", "cmp-2", "cmp-3"]
    report = CompareUtils.inspect(comparisons)
    assert report.comparisons == ["cmp-1", "cmp-2", "cmp-3"]
    assert report.timestamp
