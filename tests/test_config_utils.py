import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.config_utils import ConfigUtils


def test_config_inspect():
    configs = {"key1": "value1", "key2": "value2"}
    report = ConfigUtils.inspect(configs)
    assert report.configs == {"key1": "value1", "key2": "value2"}
    assert report.timestamp
