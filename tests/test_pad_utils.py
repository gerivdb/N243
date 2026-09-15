#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du pad_utils.py
"""

from agents.pad_utils import PadUtils


class TestPadUtils:
    def test_apply(self):
        utils = PadUtils()
        report = utils.apply([1, 2], width=4, fill=0)
        assert report.padded == [1, 2, 0, 0]
