#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du stream_utils.py
"""

from agents.stream_utils import StreamUtils


class TestStreamUtils:
    def test_inspect(self):
        utils = StreamUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.streamed == ["a"]
