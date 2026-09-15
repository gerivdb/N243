#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du token_utils.py
"""

from agents.token_utils import TokenUtils


class TestTokenUtils:
    def test_tokenize(self):
        utils = TokenUtils()
        assert utils.tokenize("a b c") == ["a", "b", "c"]

    def test_tokenize_empty(self):
        utils = TokenUtils()
        assert utils.tokenize("") == []

    def test_report(self):
        utils = TokenUtils()
        result = utils.report("a b c")
        assert result.token_count == 3
        assert result.tokens == ["a", "b", "c"]
