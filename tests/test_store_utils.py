#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du store_utils.py
"""

from agents.store_utils import StoreUtils


class TestStoreUtils:
    def test_inspect(self):
        utils = StoreUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.stored == ["a"]
