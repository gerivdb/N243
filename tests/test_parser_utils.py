#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du parser_utils.py
"""

from agents.parser_utils import ParserUtils


class TestParserUtils:
    def test_parse_line(self):
        utils = ParserUtils()
        assert utils.parse_line("a,b,c") == {"field_0": "a", "field_1": "b", "field_2": "c"}

    def test_report(self):
        utils = ParserUtils()
        report = utils.report({"field_0": "a", "field_1": "b"})
        assert report.fields == 2
