#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du templater_utils.py
"""

from agents.templater_utils import TemplaterUtils


class TestTemplaterUtils:
    def test_render(self):
        utils = TemplaterUtils()
        assert utils.render("Hello {{name}}", {"name": "World"}) == "Hello World"

    def test_report(self):
        utils = TemplaterUtils()
        report = utils.report("Hello {{name}}", "Hello World")
        assert report.template_length == 14
        assert report.rendered_length == 11
