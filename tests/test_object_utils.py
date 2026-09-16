import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.object_utils import ObjectUtils


def test_object_inspect():
    objects = ["obj-1", "obj-2", "obj-3"]
    report = ObjectUtils.inspect(objects)
    assert report.objects == ["obj-1", "obj-2", "obj-3"]
    assert report.timestamp
