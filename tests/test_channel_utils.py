#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du channel_utils.py
"""

from agents.channel_utils import ChannelUtils


class TestChannelUtils:
    def test_inspect(self):
        utils = ChannelUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.routed == ["a"]
