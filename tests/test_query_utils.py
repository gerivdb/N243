import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.query_utils import QueryUtils


def test_query_inspect():
    queries = ["query-1", "query-2", "query-3"]
    report = QueryUtils.inspect(queries)
    assert report.queries == ["query-1", "query-2", "query-3"]
    assert report.timestamp
