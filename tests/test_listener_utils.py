#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du listener_utils.py
"""

from agents.listener_utils import ListenerUtils


class TestListenerUtils:
    def test_inspect(self):
        utils = ListenerUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.listening == ["a"]
