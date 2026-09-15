#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du step_utils.py
"""

from agents.step_utils import StepUtils


class TestStepUtils:
    def test_advance(self):
        utils = StepUtils()
        report = utils.advance(["a", "b"], {"a": True, "b": False})
        assert report.advanced == ["a"]
