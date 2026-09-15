#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sampler.py
"""

from agents.sampler import Sampler


class TestSampler:
    def test_sample(self):
        sampler = Sampler(seed=42)
        result = sampler.sample(list(range(10)), 3)
        assert result.sample_size == 3
        assert result.population_size == 10
        assert len(result.items) == 3

    def test_report(self):
        sampler = Sampler()
        result = sampler.sample([1, 2, 3], 2)
        report = sampler.report(result)
        assert report["sample_size"] == 2
        assert report["population_size"] == 3
        assert abs(report["ratio"] - 2 / 3) < 1e-9
