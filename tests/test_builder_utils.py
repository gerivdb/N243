#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du builder_utils.py
"""

from agents.builder_utils import BuilderUtils


class TestBuilderUtils:
    def test_build(self):
        builder = BuilderUtils()
        builder.add("a", 1)
        builder.add("b", 2)
        assert builder.build() == {"a": 1, "b": 2}

    def test_report(self):
        builder = BuilderUtils()
        builder.add("a", 1)
        result = builder.report()
        assert result.steps == 1
        assert result.result == {"a": 1}
