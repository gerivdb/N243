import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.trace_utils import TraceUtils


def test_trace_inspect():
    traces = ["trace-1", "trace-2", "trace-3"]
    report = TraceUtils.inspect(traces)
    assert report.traces == ["trace-1", "trace-2", "trace-3"]
    assert report.timestamp
