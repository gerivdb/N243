#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du delay_utils.py
"""

from agents.delay_utils import DelayUtils


class TestDelayUtils:
    def test_defer(self):
        utils = DelayUtils()
        report = utils.defer([1, 2, 3], cycles=2)
        assert report.delayed == [1, 2, 3]
        assert report.cycles == 2
