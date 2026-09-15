#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du formatter_message_utils.py
"""

from agents.formatter_message_utils import FormatterMessageUtils


class TestFormatterMessageUtils:
    def test_format_message(self):
        utils = FormatterMessageUtils()
        assert utils.format_message("hello {name}", {"name": "world"}) == "hello world"

    def test_report(self):
        utils = FormatterMessageUtils()
        report = utils.report("hello {name}", "hello world")
        assert report.formatted == "hello world"
