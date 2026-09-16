import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.sync_utils import SyncUtils


def test_sync_inspect():
    syncs = ["sync-1", "sync-2", "sync-3"]
    report = SyncUtils.inspect(syncs)
    assert report.syncs == ["sync-1", "sync-2", "sync-3"]
    assert report.timestamp
