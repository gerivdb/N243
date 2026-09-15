#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du event_utils.py
"""

from agents.event_utils import EventUtils


class TestEventUtils:
    def test_subscribe_and_publish(self):
        bus = EventUtils()
        seen: list = []
        bus.subscribe("click", seen.append)
        bus.publish("click", 1)
        assert seen == [1]

    def test_multiple_listeners(self):
        bus = EventUtils()
        a: list = []
        b: list = []
        bus.subscribe("click", a.append)
        bus.subscribe("click", b.append)
        bus.publish("click", 2)
        assert a == [2]
        assert b == [2]

    def test_unsubscribe(self):
        bus = EventUtils()
        seen: list = []

        def handler(value):
            seen.append(value)

        bus.subscribe("click", handler)
        bus.unsubscribe("click", handler)
        bus.publish("click", 1)
        assert seen == []

    def test_listener_count(self):
        bus = EventUtils()
        bus.subscribe("click", lambda x: None)
        bus.subscribe("click", lambda x: None)
        assert bus.listener_count("click") == 2

    def test_report(self):
        bus = EventUtils()
        bus.subscribe("click", lambda x: None)
        result = bus.report("click", 1)
        assert result.event == "click"
        assert result.listeners == 1
