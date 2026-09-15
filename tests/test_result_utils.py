#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du result_utils.py
"""

from agents.result_utils import ResultUtils, Result


class TestResultUtils:
    def test_ok(self):
        result = ResultUtils.ok(42)
        assert result.success is True
        assert result.value == 42
        assert result.error is None

    def test_fail(self):
        result = ResultUtils.fail("boom")
        assert result.success is False
        assert result.value is None
        assert result.error == "boom"
