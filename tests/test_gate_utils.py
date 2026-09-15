#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du gate_utils.py
"""

from agents.gate_utils import GateUtils


class TestGateUtils:
    def test_check(self):
        utils = GateUtils()
        report = utils.check([1.0, 5.0, 3.0], threshold=3.0)
        assert report.passed == 2
        assert report.failed == 1
