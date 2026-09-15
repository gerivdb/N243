#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du scale_utils.py
"""

from agents.scale_utils import ScaleUtils


class TestScaleUtils:
    def test_apply(self):
        utils = ScaleUtils()
        report = utils.apply([1.0, 2.0, 3.0], factor=2.0)
        assert report.scaled == [2.0, 4.0, 6.0]
