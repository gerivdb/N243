import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.deduplicator_utils import DeduplicatorUtils


def test_deduplicator_inspect():
    duplicates = ["dup-1", "dup-2", "dup-3"]
    report = DeduplicatorUtils.inspect(duplicates)
    assert report.duplicates == ["dup-1", "dup-2", "dup-3"]
    assert report.timestamp
