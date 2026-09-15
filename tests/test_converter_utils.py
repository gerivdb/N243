#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du converter_utils.py
"""

from agents.converter_utils import ConverterUtils


class TestConverterUtils:
    def test_to_int_success(self):
        assert ConverterUtils.to_int("42") == 42

    def test_to_int_fallback(self):
        assert ConverterUtils.to_int("abc", 0) == 0

    def test_to_bool(self):
        assert ConverterUtils.to_bool("true") is True
        assert ConverterUtils.to_bool("no") is False

    def test_report(self):
        converter = ConverterUtils()
        result = converter.report("str", "int", True, 1)
        assert result.success is True
        assert result.value == 1
