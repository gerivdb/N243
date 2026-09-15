#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du interrupt_utils.py
"""

from agents.interrupt_utils import InterruptUtils


class TestInterruptUtils:
    def test_check(self):
        utils = InterruptUtils()
        report = utils.check([{"value": 1.0}, {"value": 5.0}], threshold=3.0)
        assert report.interrupted == 1
