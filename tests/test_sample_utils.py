#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sample_utils.py
"""

from agents.sample_utils import SampleUtils


class TestSampleUtils:
    def test_pick(self):
        utils = SampleUtils()
        report = utils.pick(["a", "b"], {"a": True, "b": False})
        assert report.sampled == ["a"]
