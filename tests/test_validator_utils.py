#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du validator_utils.py
"""

from agents.validator_utils import ValidatorUtils


class TestValidatorUtils:
    def test_required(self):
        validator = ValidatorUtils()
        assert validator.required("name", None) is not None
        assert validator.required("name", 1) is None

    def test_type_check(self):
        validator = ValidatorUtils()
        assert validator.type_check("age", 1, int) is None
        assert validator.type_check("age", "1", int) is not None

    def test_validate_valid(self):
        validator = ValidatorUtils()
        result = validator.validate(
            [
                {"name": "age", "value": 5, "required": True, "type": int, "min": 0, "max": 10},
            ]
        )
        assert result.valid is True

    def test_validate_invalid(self):
        validator = ValidatorUtils()
        result = validator.validate(
            [
                {"name": "age", "value": None, "required": True},
            ]
        )
        assert result.valid is False
