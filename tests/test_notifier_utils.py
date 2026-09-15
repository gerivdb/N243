#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du notifier_utils.py
"""

from agents.notifier_utils import NotifierUtils


class TestNotifierUtils:
    def test_subscribe_and_notify(self):
        notifier = NotifierUtils()
        seen: list = []
        notifier.subscribe("topic", seen.append)
        notifier.notify("topic", "hello")
        assert seen == ["hello"]

    def test_subscriber_count(self):
        notifier = NotifierUtils()
        notifier.subscribe("topic", lambda msg: None)
        notifier.subscribe("topic", lambda msg: None)
        assert notifier.subscriber_count("topic") == 2

    def test_report(self):
        notifier = NotifierUtils()
        notifier.subscribe("topic", lambda msg: None)
        result = notifier.report("topic", "hello")
        assert result.message == "hello"
        assert result.subscribers == 1
