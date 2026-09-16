import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.registry_utils import RegistryUtils


def test_registry_inspect():
    entries = ["entry-1", "entry-2", "entry-3"]
    report = RegistryUtils.inspect(entries)
    assert report.entries == ["entry-1", "entry-2", "entry-3"]
    assert report.timestamp
