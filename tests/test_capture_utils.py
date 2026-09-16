import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.capture_utils import CaptureUtils


def test_capture_inspect():
    captures = ["capture-1", "capture-2", "capture-3"]
    report = CaptureUtils.inspect(captures)
    assert report.captures == ["capture-1", "capture-2", "capture-3"]
    assert report.timestamp
