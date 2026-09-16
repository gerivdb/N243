import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.counter_utils import CounterUtils


def test_counter_inspect():
    counters = ["counter-1", "counter-2", "counter-3"]
    report = CounterUtils.inspect(counters)
    assert report.counters == ["counter-1", "counter-2", "counter-3"]
    assert report.timestamp
