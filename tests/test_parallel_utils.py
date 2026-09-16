import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.parallel_utils import ParallelUtils


def test_parallel_inspect():
    parallel = ["task-1", "task-2", "task-3"]
    report = ParallelUtils.inspect(parallel)
    assert report.parallel == ["task-1", "task-2", "task-3"]
    assert report.timestamp
