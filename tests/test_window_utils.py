#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du window_utils.py
"""

from agents.window_utils import WindowUtils


class TestWindowUtils:
    def test_apply(self):
        utils = WindowUtils()
        report = utils.apply([1, 2, 3, 4], size=2)
        assert report.windows == [[1, 2], [2, 3], [3, 4]]
