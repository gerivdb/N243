import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.version_utils import VersionUtils


def test_version_inspect():
    versions = ["1.0.0", "1.1.0", "2.0.0"]
    report = VersionUtils.inspect(versions)
    assert report.versions == ["1.0.0", "1.1.0", "2.0.0"]
    assert report.timestamp
