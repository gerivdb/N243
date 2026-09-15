#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du thread_utils.py
"""

from agents.thread_utils import ThreadUtils


class TestThreadUtils:
    def test_inspect(self):
        utils = ThreadUtils()
        report = utils.inspect(["t1", "t2"], {"t1": True, "t2": False})
        assert report.active == ["t1"]
