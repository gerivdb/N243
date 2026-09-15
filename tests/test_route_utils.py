#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du route_utils.py
"""

from agents.route_utils import RouteUtils


class TestRouteUtils:
    def test_select(self):
        utils = RouteUtils()
        report = utils.select(["a", "b", "c"], index=1)
        assert report.selected == "b"
        assert report.index == 1
