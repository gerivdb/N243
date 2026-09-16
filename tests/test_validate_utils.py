import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.validate_utils import ValidateUtils


def test_validate_inspect():
    valid = ["item-1", "item-2", "item-3"]
    report = ValidateUtils.inspect(valid)
    assert report.valid == ["item-1", "item-2", "item-3"]
    assert report.timestamp
