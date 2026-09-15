#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du trim_utils.py
"""

from agents.trim_utils import TrimUtils


class TestTrimUtils:
    def test_apply(self):
        utils = TrimUtils()
        report = utils.apply([1, 2, 3, 4], width=2)
        assert report.trimmed == [1, 2]
