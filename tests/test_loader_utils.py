#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du loader_utils.py
"""

from agents.loader_utils import LoaderUtils


class TestLoaderUtils:
    def test_inspect(self):
        utils = LoaderUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.loaded == ["a"]
