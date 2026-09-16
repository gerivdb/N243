import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.filter_utils import FilterUtils


def test_filter_inspect():
    filters = ["filter-1", "filter-2", "filter-3"]
    report = FilterUtils.inspect(filters)
    assert report.filters == ["filter-1", "filter-2", "filter-3"]
    assert report.timestamp
