#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sanitizer_utils.py
"""

from agents.sanitizer_utils import SanitizerUtils


class TestSanitizerUtils:
    def test_sanitize_removes_non_printable(self):
        sanitizer = SanitizerUtils()
        result = sanitizer.sanitize("a\x00b")
        assert "\x00" not in result.sanitized
        assert result.removals == 1

    def test_sanitize_allowed_chars(self):
        sanitizer = SanitizerUtils(allowed_chars="abc")
        result = sanitizer.sanitize("abc123")
        assert result.sanitized == "abc"
        assert result.removals == 3

    def test_report(self):
        sanitizer = SanitizerUtils()
        result = sanitizer.sanitize("hello")
        assert result.original == "hello"
        assert result.sanitized == "hello"
        assert result.removals == 0
