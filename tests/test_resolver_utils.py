import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.resolver_utils import ResolverUtils


def test_resolver_inspect():
    resolved = ["res-1", "res-2", "res-3"]
    report = ResolverUtils.inspect(resolved)
    assert report.resolved == ["res-1", "res-2", "res-3"]
    assert report.timestamp
