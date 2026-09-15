#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du profile_utils.py
"""

from agents.profile_utils import ProfileUtils


class TestProfileUtils:
    def test_measure(self):
        utils = ProfileUtils()
        report = utils.measure(["a", "b"], {"a": 1, "b": None})
        assert report.profiled == ["a"]
