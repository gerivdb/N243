import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.work_utils import WorkUtils


def test_work_inspect():
    items = ["w1", "w2", "w3"]
    report = WorkUtils.inspect(items)
    assert report.items == ["w1", "w2", "w3"]
    assert report.timestamp
