#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du multiplier_utils.py
"""

from agents.multiplier_utils import MultiplierUtils


class TestMultiplierUtils:
    def test_multiply_numbers(self):
        assert MultiplierUtils.multiply_numbers([2, 3, 4]) == 24.0

    def test_multiply_lists(self):
        assert MultiplierUtils.multiply_lists([1, 2], ["a", "b"]) == [
            "1a", "1b", "2a", "2b"
        ]

    def test_report(self):
        utils = MultiplierUtils()
        result = utils.report([2, 3], 6)
        assert result.result == 6
        assert len(result.inputs) == 2
