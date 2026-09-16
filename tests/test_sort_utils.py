import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.sort_utils import SortUtils


def test_sort_inspect():
    items = ["c", "a", "b"]
    report = SortUtils.inspect(items)
    assert report.sorted_items == ["a", "b", "c"]
    assert report.timestamp
