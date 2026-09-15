#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du trigger_utils.py
"""

from agents.trigger_utils import TriggerUtils


class TestTriggerUtils:
    def test_evaluate(self):
        utils = TriggerUtils()
        report = utils.evaluate([1.0, 5.0, 3.0], threshold=3.0)
        assert report.triggered == 2
