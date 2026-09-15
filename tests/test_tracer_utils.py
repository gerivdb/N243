#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du tracer_utils.py
"""

from agents.tracer_utils import TracerUtils


class TestTracerUtils:
    def test_follow(self):
        utils = TracerUtils()
        report = utils.follow(["a", "b"], {"a": 1, "b": None})
        assert report.traced == ["a"]
