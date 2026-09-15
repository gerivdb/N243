#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du memory_utils.py
"""

from agents.memory_utils import MemoryUtils


class TestMemoryUtils:
    def test_store(self):
        utils = MemoryUtils()
        report = utils.store(["a", "b"], {"a": 1, "b": None})
        assert report.stored == ["a"]
