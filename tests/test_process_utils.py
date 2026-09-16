import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.process_utils import ProcessUtils


def test_process_inspect():
    processes = ["proc-1", "proc-2", "proc-3"]
    report = ProcessUtils.inspect(processes)
    assert report.processes == ["proc-1", "proc-2", "proc-3"]
    assert report.timestamp
