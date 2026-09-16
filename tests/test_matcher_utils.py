#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du matcher_utils.py
"""

from agents.matcher_utils import MatcherUtils, MatcherReport


class TestMatcherUtils:
    def test_matches(self):
        assert MatcherUtils.matches("hello world", "world") is True
        assert MatcherUtils.matches("hello world", "xyz") is False

    def test_find_all(self):
        result = MatcherUtils.find_all("a1b2c3", r"\d")
        assert result == ["1", "2", "3"]

    def test_replace(self):
        result = MatcherUtils.replace("hello world", "world", "python")
        assert result == "hello python"

    def test_report(self):
        r = MatcherUtils.report("hello", "hel")
        assert r.text == "hello"
        assert r.pattern == "hel"
        assert r.matched is True
        assert r.timestamp
