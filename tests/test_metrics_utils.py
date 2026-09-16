import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.metrics_utils import MetricsUtils


def test_metrics_inspect():
    metrics = ["metric-1", "metric-2", "metric-3"]
    report = MetricsUtils.inspect(metrics)
    assert report.metrics == ["metric-1", "metric-2", "metric-3"]
    assert report.timestamp
