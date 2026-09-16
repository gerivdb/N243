#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du router_utils.py
"""

from agents.router_utils import RouterUtils


class TestRouterUtils:
    def test_inspect(self):
        utils = RouterUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.routed == ["a"]
