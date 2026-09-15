#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du guard_utils.py
"""

from agents.guard_utils import GuardUtils


class TestGuardUtils:
    def test_required(self):
        guard = GuardUtils()
        assert guard.required("name", None) is not None
        assert guard.required("name", 1) is None

    def test_type_check(self):
        guard = GuardUtils()
        assert guard.type_check("age", 1, int) is None
        assert guard.type_check("age", "1", int) is not None

    def test_range_check(self):
        guard = GuardUtils()
        assert guard.range_check("age", 5, 0, 10) is None
        assert guard.range_check("age", 11, 0, 10) is not None

    def test_run_valid(self):
        guard = GuardUtils()
        result = guard.run(
            [
                {"name": "age", "value": 5, "required": True, "type": int, "min": 0, "max": 10},
            ]
        )
        assert result.valid is True

    def test_run_invalid(self):
        guard = GuardUtils()
        result = guard.run(
            [
                {"name": "age", "value": None, "required": True},
            ]
        )
        assert result.valid is False
        assert len(result.errors) == 1
