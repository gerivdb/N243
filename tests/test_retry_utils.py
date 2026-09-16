import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.retry_utils import RetryUtils


def test_retry_inspect():
    retried = ["op-1", "op-2", "op-3"]
    report = RetryUtils.inspect(retried)
    assert report.retried == ["op-1", "op-2", "op-3"]
    assert report.timestamp
