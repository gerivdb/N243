#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du gateway_utils.py
"""

from agents.gateway_utils import GatewayUtils


class TestGatewayUtils:
    def test_inspect(self):
        utils = GatewayUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.routed == ["a"]
