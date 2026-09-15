#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du latch_utils.py
"""

from agents.latch_utils import LatchUtils


class TestLatchUtils:
    def test_evaluate(self):
        utils = LatchUtils()
        report = utils.evaluate([1.0, 5.0, 3.0], threshold=3.0)
        assert report.latched == 2
