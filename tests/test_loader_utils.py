#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du loader_utils.py
"""

from agents.loader_utils import LoaderUtils


class TestLoaderUtils:
    def test_load_from_dict(self):
        loader = LoaderUtils()
        source = {"a": 1, "b": 2}
        assert loader.load_from_dict(source) == {"a": 1, "b": 2}

    def test_load_items(self):
        loader = LoaderUtils()
        assert loader.load_items({"a": 1, "b": 2}) == [1, 2]

    def test_report(self):
        loader = LoaderUtils()
        report = loader.report("dict", 2)
        assert report.loaded == 2
        assert report.source == "dict"
