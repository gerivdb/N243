#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du buffer_utils.py
"""

from agents.buffer_utils import BufferUtils


class TestBufferUtils:
    def test_inspect(self):
        utils = BufferUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.buffered == ["a"]
