import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.log_utils import LogUtils


def test_log_inspect():
    logs = ["log-1", "log-2", "log-3"]
    report = LogUtils.inspect(logs)
    assert report.logs == ["log-1", "log-2", "log-3"]
    assert report.timestamp
