#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du job_utils.py
"""

from agents.job_utils import JobUtils


class TestJobUtils:
    def test_queue(self):
        utils = JobUtils()
        report = utils.queue(["build", "test"], {"build": 1, "test": None})
        assert report.queued == ["build"]
