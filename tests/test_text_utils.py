#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du text_utils.py
"""

from agents.text_utils import TextUtils, TextReport


class TestTextUtils:
    def test_word_count(self):
        assert TextUtils.word_count("hello world") == 2

    def test_char_count(self):
        assert TextUtils.char_count("abc") == 3

    def test_find_all(self):
        assert TextUtils.find_all("a1 b2 c3", r"\d") == ["1", "2", "3"]

    def test_replace_all(self):
        assert TextUtils.replace_all("a a a", "a", "b") == "b b b"

    def test_report(self):
        r = TextUtils.report("word_count", "2")
        assert r.operation == "word_count"
        assert r.result == "2"
        assert r.timestamp
