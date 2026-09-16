import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.memory_utils import MemoryUtils


def test_memory_inspect():
    blocks = ["block-1", "block-2", "block-3"]
    report = MemoryUtils.inspect(blocks)
    assert report.blocks == ["block-1", "block-2", "block-3"]
    assert report.timestamp
