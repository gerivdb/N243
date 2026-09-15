#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du debug_utils.py
"""

from agents.debug_utils import DebugUtils


class TestDebugUtils:
    def test_inspect(self):
        utils = DebugUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.issues == ["b"]
