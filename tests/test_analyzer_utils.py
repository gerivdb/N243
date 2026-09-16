import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.analyzer_utils import AnalyzerUtils


def test_analyzer_inspect():
    analyzed = ["item-1", "item-2", "item-3"]
    report = AnalyzerUtils.inspect(analyzed)
    assert report.analyzed == ["item-1", "item-2", "item-3"]
    assert report.timestamp
