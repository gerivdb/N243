import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.cache_utils import CacheUtils


def test_cache_inspect():
    keys = ["cache-key-1", "cache-key-2", "cache-key-3"]
    report = CacheUtils.inspect(keys)
    assert report.keys == ["cache-key-1", "cache-key-2", "cache-key-3"]
    assert report.timestamp
