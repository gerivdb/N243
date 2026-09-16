import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.ordered_utils import OrderedUtils


def test_ordered_inspect():
    ordered = ["item-1", "item-2", "item-3"]
    report = OrderedUtils.inspect(ordered)
    assert report.ordered == ["item-1", "item-2", "item-3"]
    assert report.timestamp
