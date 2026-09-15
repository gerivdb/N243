#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du notifier_utils.py
"""

from agents.notifier_utils import NotifierUtils


class TestNotifierUtils:
    def test_send(self):
        utils = NotifierUtils()
        report = utils.send(["a", "b"], {"a": True, "b": False})
        assert report.notified == ["a"]
