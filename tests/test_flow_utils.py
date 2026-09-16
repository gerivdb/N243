import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.flow_utils import FlowUtils


def test_flow_inspect():
    flows = ["flow-1", "flow-2", "flow-3"]
    report = FlowUtils.inspect(flows)
    assert report.flows == ["flow-1", "flow-2", "flow-3"]
    assert report.timestamp
