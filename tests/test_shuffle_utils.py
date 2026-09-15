#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du shuffle_utils.py
"""

from agents.shuffle_utils import ShuffleUtils


class TestShuffleUtils:
    def test_apply(self):
        utils = ShuffleUtils()
        values = [1, 2, 3]
        report = utils.apply(values)
        assert set(report.shuffled) == set(values)
        assert len(report.shuffled) == len(values)
