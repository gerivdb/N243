#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du spectrum_utils.py
"""

from agents.spectrum_utils import SpectrumUtils


class TestSpectrumUtils:
    def test_amplitudes(self):
        utils = SpectrumUtils()
        assert utils.amplitudes([-1.0, 2.0, -3.0]) == [1.0, 2.0, 3.0]

    def test_report(self):
        utils = SpectrumUtils()
        report = utils.report([-1.0, 2.0, -3.0])
        assert report.max_amplitude == 3.0
