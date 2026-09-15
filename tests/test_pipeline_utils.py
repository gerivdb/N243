#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du pipeline_utils.py
"""

from agents.pipeline_utils import PipelineUtils


class TestPipelineUtils:
    def test_run(self):
        utils = PipelineUtils()
        report = utils.run(["a", "b"], {"a": True, "b": False})
        assert report.completed == 1
        assert report.stages == ["a", "b"]
