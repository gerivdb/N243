import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.bus_utils import BusUtils


def test_bus_inspect():
    messages = ["msg-1", "msg-2", "msg-3"]
    report = BusUtils.inspect(messages)
    assert report.messages == ["msg-1", "msg-2", "msg-3"]
    assert report.timestamp
