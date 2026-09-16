import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.merge_utils import MergeUtils


def test_merge_inspect():
    merges = ["merge-1", "merge-2", "merge-3"]
    report = MergeUtils.inspect(merges)
    assert report.merges == ["merge-1", "merge-2", "merge-3"]
    assert report.timestamp
