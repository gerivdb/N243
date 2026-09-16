import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.context_utils import ContextUtils


def test_context_inspect():
    contexts = ["ctx-1", "ctx-2", "ctx-3"]
    report = ContextUtils.inspect(contexts)
    assert report.contexts == ["ctx-1", "ctx-2", "ctx-3"]
    assert report.timestamp
