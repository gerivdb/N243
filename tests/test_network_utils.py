import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.network_utils import NetworkUtils


def test_network_inspect():
    connections = ["conn-1", "conn-2", "conn-3"]
    report = NetworkUtils.inspect(connections)
    assert report.connections == ["conn-1", "conn-2", "conn-3"]
    assert report.timestamp
