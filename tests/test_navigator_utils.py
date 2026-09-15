#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du navigator_utils.py
"""

from agents.navigator_utils import NavigatorUtils


class TestNavigatorUtils:
    def test_get_by_path_found(self):
        data = {"a": {"b": {"c": 1}}}
        assert NavigatorUtils.get_by_path(data, "a.b.c") == 1

    def test_get_by_path_missing(self):
        data = {"a": {"b": 1}}
        assert NavigatorUtils.get_by_path(data, "a.c", default=0) == 0

    def test_report(self):
        utils = NavigatorUtils()
        report = utils.report("a.b", True, 1)
        assert report.path == "a.b"
        assert report.found is True
