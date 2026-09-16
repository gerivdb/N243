import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.state_utils import StateUtils


def test_state_inspect():
    states = ["idle", "running", "stopped"]
    report = StateUtils.inspect(states)
    assert report.states == ["idle", "running", "stopped"]
    assert report.timestamp
