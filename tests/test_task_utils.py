import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.task_utils import TaskUtils


def test_task_inspect():
    tasks = ["build", "test", "publish"]
    report = TaskUtils.inspect(tasks)
    assert report.scheduled == ["build", "test", "publish"]
    assert report.timestamp
