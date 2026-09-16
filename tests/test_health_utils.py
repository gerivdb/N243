import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.health_utils import HealthUtils


def test_health_inspect():
    checks = ["health-1", "health-2", "health-3"]
    report = HealthUtils.inspect(checks)
    assert report.checks == ["health-1", "health-2", "health-3"]
    assert report.timestamp
