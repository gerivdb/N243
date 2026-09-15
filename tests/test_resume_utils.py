#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du resume_utils.py
"""

from agents.resume_utils import ResumeUtils


class TestResumeUtils:
    def test_filter(self):
        utils = ResumeUtils()
        report = utils.filter([{"value": 1, "resume": True}, {"value": 2, "resume": False}])
        assert report.resumed == [1]
