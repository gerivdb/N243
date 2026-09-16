import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.builder_utils import BuilderUtils


def test_builder_inspect():
    builds = ["build-1", "build-2", "build-3"]
    report = BuilderUtils.inspect(builds)
    assert report.builds == ["build-1", "build-2", "build-3"]
    assert report.timestamp
