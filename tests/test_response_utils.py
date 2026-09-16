import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.response_utils import ResponseUtils


def test_response_inspect():
    responses = ["resp-1", "resp-2", "resp-3"]
    report = ResponseUtils.inspect(responses)
    assert report.responses == ["resp-1", "resp-2", "resp-3"]
    assert report.timestamp
