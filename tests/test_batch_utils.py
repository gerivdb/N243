import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.batch_utils import BatchUtils


def test_batch_inspect():
    batches = ["batch-1", "batch-2", "batch-3"]
    report = BatchUtils.inspect(batches)
    assert report.batches == ["batch-1", "batch-2", "batch-3"]
    assert report.timestamp
