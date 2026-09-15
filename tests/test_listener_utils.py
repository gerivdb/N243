#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du listener_utils.py
"""

from agents.listener_utils import ListenerUtils


class TestListenerUtils:
    def test_on_and_emit(self):
        listener = ListenerUtils()
        seen: list = []
        listener.on("click", seen.append)
        listener.emit("click", 1)
        assert seen == [1]

    def test_listener_count(self):
        listener = ListenerUtils()
        listener.on("click", lambda x: None)
        listener.on("click", lambda x: None)
        assert listener.listener_count("click") == 2

    def test_report(self):
        listener = ListenerUtils()
        listener.on("click", lambda x: None)
        result = listener.report("click", 1)
        assert result.event == "click"
        assert result.listeners_called == 1
