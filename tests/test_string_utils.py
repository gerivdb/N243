#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du string_utils.py
"""

from agents.string_utils import StringUtils, StringReport


class TestStringUtils:
    def test_slugify(self):
        assert StringUtils.slugify("Hello World!") == "hello-world"

    def test_truncate(self):
        assert StringUtils.truncate("hello world", 5) == "he..."
        assert StringUtils.truncate("hello", 10) == "hello"

    def test_split_preserve(self):
        assert StringUtils.split_preserve("a,b,c", ",") == ["a", "b", "c"]
        assert StringUtils.split_preserve("", ",") == []

    def test_report(self):
        r = StringUtils.report("slugify", "hello-world")
        assert r.operation == "slugify"
        assert r.result == "hello-world"
        assert r.timestamp
