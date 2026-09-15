#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du switch_utils.py
"""

from agents.switch_utils import SwitchUtils


class TestSwitchUtils:
    def test_select(self):
        utils = SwitchUtils()
        report = utils.select({"a": False, "b": "value_b"})
        assert report.selected == "value_b"
        assert report.condition == "b"

    def test_default(self):
        utils = SwitchUtils()
        report = utils.select({"a": False, "b": False}, default="default_value")
        assert report.selected == "default_value"
