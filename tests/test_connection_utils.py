#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du connection_utils.py
"""

from agents.connection_utils import ConnectionUtils


class TestConnectionUtils:
    def test_inspect(self):
        utils = ConnectionUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.connected == ["a"]
