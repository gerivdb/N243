#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du waveform_utils.py
"""

from agents.waveform_utils import WaveformUtils


class TestWaveformUtils:
    def test_sine(self):
        utils = WaveformUtils()
        samples = utils.sine(length=4)
        assert len(samples) == 4
        assert abs(samples[0]) < 1e-6

    def test_report(self):
        utils = WaveformUtils()
        report = utils.report(length=4)
        assert report.samples == 4
