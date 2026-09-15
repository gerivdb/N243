#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du unloader_utils.py
"""

from agents.unloader_utils import UnloaderUtils


class TestUnloaderUtils:
    def test_unload_keys(self):
        assert UnloaderUtils.unload_keys({"a": 1, "b": 2}) == ["a", "b"]

    def test_unload_values(self):
        assert UnloaderUtils.unload_values({"a": 1, "b": 2}) == [1, 2]

    def test_report(self):
        utils = UnloaderUtils()
        report = utils.report("dict", 2)
        assert report.unloaded == 2
        assert report.source == "dict"
