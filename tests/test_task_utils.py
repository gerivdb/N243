#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du task_utils.py
"""

from agents.task_utils import TaskUtils


class TestTaskUtils:
    def test_complete(self):
        utils = TaskUtils()
        report = utils.complete(["a", "b"], {"a": True, "b": False})
        assert report.completed == ["a"]
