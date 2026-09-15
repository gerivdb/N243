#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du workflow_utils.py
"""

from agents.workflow_utils import WorkflowUtils


class TestWorkflowUtils:
    def test_run(self):
        utils = WorkflowUtils()
        report = utils.run(["a", "b"], {"a": True, "b": False})
        assert report.executed == ["a"]
