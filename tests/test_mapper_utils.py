#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du mapper_utils.py
"""

from agents.mapper_utils import MapperUtils


class TestMapperUtils:
    def test_map_found(self):
        mapper = MapperUtils({1: "one", 2: "two"})
        result = mapper.map(1)
        assert result.output_value == "one"
        assert result.mapped is True

    def test_map_missing(self):
        mapper = MapperUtils({1: "one"})
        result = mapper.map(2, default="missing")
        assert result.output_value == "missing"
        assert result.mapped is False

    def test_keys(self):
        mapper = MapperUtils({1: "one", 2: "two"})
        assert set(mapper.keys()) == {1, 2}
