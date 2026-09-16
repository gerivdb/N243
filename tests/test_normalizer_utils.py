#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du normalizer_utils.py
"""

from agents.normalizer_utils import NormalizerUtils, NormalizerReport


class TestNormalizerUtils:
    def test_lowercase(self):
        assert NormalizerUtils.lowercase("HELLO") == "hello"

    def test_strip(self):
        assert NormalizerUtils.strip("  hello  ") == "hello"

    def test_collapse_spaces(self):
        assert NormalizerUtils.collapse_spaces("hello    world") == "hello world"

    def test_normalize(self):
        result = NormalizerUtils.normalize("  HELLO    WORLD  ")
        assert result == "hello world"

    def test_report(self):
        r = NormalizerUtils.report("  HELLO  ")
        assert r.original == "  HELLO  "
        assert r.normalized == "hello"
        assert r.timestamp
