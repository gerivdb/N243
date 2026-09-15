#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sampler_utils.py
"""

from agents.sampler_utils import SamplerUtils
import pytest


class TestSamplerUtils:
    def test_sample(self):
        utils = SamplerUtils()
        sample = utils.sample([1, 2, 3, 4, 5], 3)
        assert len(sample) == 3
        assert all(item in [1, 2, 3, 4, 5] for item in sample)

    def test_sample_invalid_size(self):
        utils = SamplerUtils()
        with pytest.raises(ValueError):
            utils.sample([1, 2], 3)

    def test_report(self):
        utils = SamplerUtils()
        result = utils.report([1, 2, 3], 2)
        assert result.population_size == 3
        assert result.sample_size == 2
