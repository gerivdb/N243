#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du io_utils.py
"""

from agents.io_utils import IOUtils


class TestIOUtils:
    def test_trace(self):
        utils = IOUtils()
        report = utils.trace(["a", "b"], {"a": 1, "b": True})
        assert report.inputs == ["a", "b"]
        assert report.outputs == ["b"]
