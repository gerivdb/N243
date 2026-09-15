#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du validation_utils.py
"""

from agents.validation_utils import ValidationUtils


class TestValidationUtils:
    def test_is_number(self):
        utils = ValidationUtils()
        assert utils.is_number(1) is True
        assert utils.is_number("a") is False

    def test_in_range(self):
        utils = ValidationUtils()
        assert utils.in_range(5, 0, 10) is True
        assert utils.in_range(11, 0, 10) is False

    def test_matches_pattern(self):
        utils = ValidationUtils()
        assert utils.matches_pattern("abc123", r"\d+") is True
        assert utils.matches_pattern("abc", r"\d+") is False

    def test_validate_valid(self):
        utils = ValidationUtils()
        result = utils.validate(
            {
                "age": {"value": 25, "type": "number", "min": 0, "max": 120},
                "code": {"value": "A1B2", "pattern": r"[A-Z]\d"},
            }
        )
        assert result.valid is True

    def test_validate_invalid(self):
        utils = ValidationUtils()
        result = utils.validate(
            {
                "age": {"value": -1, "type": "number", "min": 0, "max": 120},
            }
        )
        assert result.valid is False
        assert len(result.errors) == 1
