#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du phase_utils.py
"""

from agents.phase_utils import PhaseUtils


class TestPhaseUtils:
    def test_normalize(self):
        utils = PhaseUtils()
        assert utils.normalize([0.0, 5.0, 10.0]) == [0.0, 0.5, 1.0]

    def test_report(self):
        utils = PhaseUtils()
        report = utils.report([0.0, 5.0, 10.0])
        assert report.phase == 0.0
