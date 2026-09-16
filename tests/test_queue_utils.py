#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du queue_utils.py
"""

from agents.queue_utils import QueueUtils


class TestQueueUtils:
    def test_inspect(self):
        utils = QueueUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.queued == ["a"]
