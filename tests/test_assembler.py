#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du assembler.py
"""

from agents.assembler import Assembler


class TestAssembler:
    def test_assemble(self):
        assembler = Assembler(["a", "b"])
        result = assembler.assemble([{"a": 1}, {"b": 2}])
        assert result.assembled == {"a": 1, "b": 2}
        assert result.missing_fields == []

    def test_assemble_missing(self):
        assembler = Assembler(["a", "b", "c"])
        result = assembler.assemble([{"a": 1}])
        assert result.missing_fields == ["b", "c"]

    def test_is_complete(self):
        assembler = Assembler(["a", "b"])
        assert assembler.is_complete([{"a": 1}, {"b": 2}]) is True
        assert assembler.is_complete([{"a": 1}]) is False
