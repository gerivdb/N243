import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.checker_utils import CheckerUtils


def test_checker_inspect():
    checks = ["check-1", "check-2", "check-3"]
    report = CheckerUtils.inspect(checks)
    assert report.checks == ["check-1", "check-2", "check-3"]
    assert report.timestamp
