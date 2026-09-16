import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.collection_utils import CollectionUtils


def test_collection_inspect():
    collections = ["col-1", "col-2", "col-3"]
    report = CollectionUtils.inspect(collections)
    assert report.collections == ["col-1", "col-2", "col-3"]
    assert report.timestamp
