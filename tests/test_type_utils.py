#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du type_utils.py
"""

from agents.type_utils import TypeUtils, TypeReport


class TestTypeUtils:
    def test_is_list(self):
        assert TypeUtils.is_list([1, 2]) is True
        assert TypeUtils.is_list("abc") is False

    def test_is_dict(self):
        assert TypeUtils.is_dict({"a": 1}) is True
        assert TypeUtils.is_dict([]) is False

    def test_is_str(self):
        assert TypeUtils.is_str("abc") is True
        assert TypeUtils.is_str(123) is False

    def test_is_int(self):
        assert TypeUtils.is_int(1) is True
        assert TypeUtils.is_int(True) is False
        assert TypeUtils.is_int(1.5) is False

    def test_is_float(self):
        assert TypeUtils.is_float(1.5) is True
        assert TypeUtils.is_float(1) is False

    def test_is_bool(self):
        assert TypeUtils.is_bool(True) is True
        assert TypeUtils.is_bool(1) is False

    def test_type_name(self):
        assert TypeUtils.type_name(1) == "int"
        assert TypeUtils.type_name("abc") == "str"

    def test_report(self):
        r = TypeUtils.report(42)
        assert r.value == 42
        assert r.type_name == "int"
        assert r.timestamp
