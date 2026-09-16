import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.security_utils import SecurityUtils


def test_security_inspect():
    checks = ["check-1", "check-2", "check-3"]
    report = SecurityUtils.inspect(checks)
    assert report.checks == ["check-1", "check-2", "check-3"]
    assert report.timestamp
