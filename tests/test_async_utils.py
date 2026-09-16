import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.async_utils import AsyncUtils


def test_async_inspect():
    operations = ["op-1", "op-2", "op-3"]
    report = AsyncUtils.inspect(operations)
    assert report.operations == ["op-1", "op-2", "op-3"]
    assert report.timestamp
