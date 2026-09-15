#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du error_utils.py
"""

from agents.error_utils import ErrorUtils


class TestErrorUtils:
    def test_collect(self):
        utils = ErrorUtils()
        report = utils.collect(["a", "b"], {"a": True, "b": False})
        assert report.errors == ["a"]
