#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du shaper_utils.py
"""

from agents.shaper_utils import ShaperUtils


class TestShaperUtils:
    def test_shape(self):
        utils = ShaperUtils()
        data = {"a": 1, "b": 2}
        mold = {"a": 0, "c": 3}
        assert utils.shape(data, mold) == {"a": 0, "b": 2}

    def test_report(self):
        utils = ShaperUtils()
        report = utils.report(2)
        assert report.shaped == 2
