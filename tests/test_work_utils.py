#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du work_utils.py
"""

from agents.work_utils import WorkUtils


class TestWorkUtils:
    def test_process(self):
        utils = WorkUtils()
        report = utils.process(["a", "b"], {"a": 1})
        assert report.processed == 1
        assert report.items == ["a", "b"]
