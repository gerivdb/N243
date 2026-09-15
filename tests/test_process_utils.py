#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du process_utils.py
"""

from agents.process_utils import ProcessUtils


class TestProcessUtils:
    def test_run(self):
        utils = ProcessUtils()
        report = utils.run(["a", "b"], {"a": True, "b": False})
        assert report.processed == ["a"]
        assert report.failed == ["b"]
