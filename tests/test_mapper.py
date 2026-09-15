#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du mapper.py
"""

from agents.mapper import Mapper


class TestMapper:
    def test_map(self):
        mapper = Mapper({"src_name": "name", "src_value": "value"})
        result = mapper.map({"src_name": "test", "src_value": 1, "extra": 2})
        assert result.target == {"name": "test", "value": 1}
        assert result.mapped_fields == ["name", "value"]
        assert result.skipped_fields == []

    def test_map_with_missing_fields(self):
        mapper = Mapper({"src_name": "name", "src_value": "value"})
        result = mapper.map({"extra": 2})
        assert result.target == {}
        assert result.skipped_fields == ["src_name", "src_value"]
