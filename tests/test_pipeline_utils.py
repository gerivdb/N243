#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du pipeline_utils.py
"""

from agents.pipeline_utils import PipelineUtils


class TestPipelineUtils:
    def test_run(self):
        pipeline = PipelineUtils([lambda x: x + 1, lambda x: x * 2])
        assert pipeline.run(1) == 4

    def test_run_with_reports(self):
        pipeline = PipelineUtils([lambda x: x + 1, lambda x: x * 2])
        value, reports = pipeline.run_with_reports(1)
        assert value == 4
        assert len(reports) == 2
        assert reports[0].output == 2
        assert reports[1].output == 4
