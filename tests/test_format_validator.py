#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du format_validator.py
"""

from agents.format_validator import FormatValidator


class TestFormatValidator:
    def test_validate_email(self):
        validator = FormatValidator()
        result = validator.validate_email("email", "user@example.com")
        assert result.valid is True
        assert result.reason == "valid"

    def test_validate_email_invalid(self):
        validator = FormatValidator()
        result = validator.validate_email("email", "invalid")
        assert result.valid is False
        assert result.reason == "invalid email format"

    def test_validate_uuid(self):
        validator = FormatValidator()
        result = validator.validate_uuid("id", "550e8400-e29b-41d4-a716-446655440000")
        assert result.valid is True

    def test_validate_regex(self):
        validator = FormatValidator()
        result = validator.validate_regex("code", "ABC123", r"^[A-Z]{3}\d{3}$")
        assert result.valid is True
