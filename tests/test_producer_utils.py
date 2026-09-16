import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.producer_utils import ProducerUtils


def test_producer_inspect():
    targets = ["a", "b", "c"]
    payload = {"a": True, "b": False, "c": True}
    report = ProducerUtils.inspect(targets, payload)
    assert report.produced == ["a", "c"]
    assert report.timestamp
