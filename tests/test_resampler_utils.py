#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du resampler_utils.py
"""

from agents.resampler_utils import ResamplerUtils


class TestResamplerUtils:
    def test_downsample(self):
        utils = ResamplerUtils()
        assert utils.downsample([1, 2, 3, 4], step=2) == [1, 3]

    def test_report(self):
        utils = ResamplerUtils()
        report = utils.report([1, 2, 3, 4], step=2)
        assert report.original_count == 4
        assert report.resampled_count == 2
