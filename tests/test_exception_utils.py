#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du exception_utils.py
"""

from agents.exception_utils import ExceptionUtils


class TestExceptionUtils:
    def test_track(self):
        utils = ExceptionUtils()
        report = utils.track(["a", "b"], {"a": True, "b": False})
        assert report.caught == ["a"]
