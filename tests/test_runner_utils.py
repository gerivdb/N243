#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du runner_utils.py
"""

from agents.runner_utils import RunnerUtils


class TestRunnerUtils:
    def test_run(self):
        utils = RunnerUtils()
        report = utils.run(["a", "b"], {"a": 1, "b": 2})
        assert report.executed == 2
        assert report.steps == ["a", "b"]
