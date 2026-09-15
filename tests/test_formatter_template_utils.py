#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du formatter_template_utils.py
"""

from agents.formatter_template_utils import FormatterTemplateUtils


class TestFormatterTemplateUtils:
    def test_render(self):
        utils = FormatterTemplateUtils()
        assert utils.render("hello {name}", {"name": "world"}) == "hello world"

    def test_report(self):
        utils = FormatterTemplateUtils()
        report = utils.report("hello {name}", "hello world")
        assert report.rendered == "hello world"
