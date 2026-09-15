#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du stack_utils.py
"""

from agents.stack_utils import StackUtils


class TestStackUtils:
    def test_depth(self):
        utils = StackUtils()
        report = utils.depth([1, 2, 3])
        assert report.depth == 3
