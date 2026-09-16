import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.channel_utils import ChannelUtils


def test_channel_inspect():
    channels = ["ch-1", "ch-2", "ch-3"]
    report = ChannelUtils.inspect(channels)
    assert report.channels == ["ch-1", "ch-2", "ch-3"]
    assert report.timestamp
