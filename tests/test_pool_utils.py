#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du pool_utils.py
"""

from agents.pool_utils import PoolUtils


class TestPoolUtils:
    def test_inspect(self):
        utils = PoolUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.pooled == ["a"]
