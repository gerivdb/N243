import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.event_utils import EventUtils


def test_event_inspect():
    events = ["evt-1", "evt-2", "evt-3"]
    report = EventUtils.inspect(events)
    assert report.events == ["evt-1", "evt-2", "evt-3"]
    assert report.timestamp
