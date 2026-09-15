#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du circuit_utils.py
"""

from agents.circuit_utils import CircuitUtils


class TestCircuitUtils:
    def test_evaluate(self):
        utils = CircuitUtils()
        report = utils.evaluate(["a", "b", "c", "d"], path=[0, 2, 3])
        assert report.path == ["a", "c", "d"]
