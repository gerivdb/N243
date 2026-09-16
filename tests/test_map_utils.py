import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.map_utils import MapUtils


def test_map_inspect():
    mappings = {"key1": "value1", "key2": "value2"}
    report = MapUtils.inspect(mappings)
    assert report.mappings == {"key1": "value1", "key2": "value2"}
    assert report.timestamp
