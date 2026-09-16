import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.bag_utils import BagUtils


def test_bag_inspect():
    bags = ["bag-1", "bag-2", "bag-3"]
    report = BagUtils.inspect(bags)
    assert report.bags == ["bag-1", "bag-2", "bag-3"]
    assert report.timestamp
