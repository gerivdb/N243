import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.mapper_utils import MapperUtils


def test_mapper_inspect():
    mappings = ["map-1", "map-2", "map-3"]
    report = MapperUtils.inspect(mappings)
    assert report.mappings == ["map-1", "map-2", "map-3"]
    assert report.timestamp
