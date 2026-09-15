#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du checker_utils.py
"""

from agents.checker_utils import CheckerUtils


class TestCheckerUtils:
    def test_check_pass(self):
        checker = CheckerUtils()
        result = checker.check("positive", lambda: 1 > 0)
        assert result.passed is True

    def test_check_fail(self):
        checker = CheckerUtils()
        result = checker.check("negative", lambda: 1 > 10)
        assert result.passed is False

    def test_run(self):
        checker = CheckerUtils()
        results = checker.run({"a": lambda: True, "b": lambda: False})
        assert results[0].passed is True
        assert results[1].passed is False
