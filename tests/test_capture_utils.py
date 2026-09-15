#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du capture_utils.py
"""

from agents.capture_utils import CaptureUtils


class TestCaptureUtils:
    def test_above(self):
        utils = CaptureUtils()
        report = utils.above([1.0, 5.0, 3.0], threshold=3.0)
        assert report.captured == [5.0]
