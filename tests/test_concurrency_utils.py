import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.concurrency_utils import ConcurrencyUtils


def test_concurrency_inspect():
    tasks = ["task-1", "task-2", "task-3"]
    report = ConcurrencyUtils.inspect(tasks)
    assert report.tasks == ["task-1", "task-2", "task-3"]
    assert report.timestamp
