#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du view_utils.py
"""

from agents.view_utils import ViewUtils


class TestViewUtils:
    def test_render(self):
        utils = ViewUtils()
        report = utils.render(["a", "b"], {"a": 1, "b": None})
        assert report.rendered == ["a"]
