#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du stage_utils.py
"""

from agents.stage_utils import StageUtils


class TestStageUtils:
    def test_advance(self):
        utils = StageUtils()
        report = utils.advance(["a", "b"], {"a": True, "b": False})
        assert report.reached == ["a"]
