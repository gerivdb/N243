import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.accumulator_utils import AccumulatorUtils


def test_accumulator_inspect():
    values = ["acc-1", "acc-2", "acc-3"]
    report = AccumulatorUtils.inspect(values)
    assert report.values == ["acc-1", "acc-2", "acc-3"]
    assert report.timestamp
