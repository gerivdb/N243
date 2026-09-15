#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du envelope_utils.py
"""

from agents.envelope_utils import EnvelopeUtils


class TestEnvelopeUtils:
    def test_bounds(self):
        utils = EnvelopeUtils()
        report = utils.bounds([1.0, 5.0, 3.0])
        assert report.upper == 5.0
        assert report.lower == 1.0
