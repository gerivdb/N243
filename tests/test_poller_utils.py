#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du poller_utils.py
"""

from agents.poller_utils import PollerUtils, PollerReport


class TestPollerUtils:
    def test_poll_immediate(self):
        result = PollerUtils.poll(lambda: "immediate", timeout=1.0, interval=0.1)
        assert result == "immediate"

    def test_poll_timeout(self):
        result = PollerUtils.poll(lambda: None, timeout=0.5, interval=0.1)
        assert result is None

    def test_report(self):
        r = PollerUtils.report("test_func", "ok", 3, True)
        assert r.func_name == "test_func"
        assert r.result == "ok"
        assert r.attempts == 3
        assert r.success is True
        assert r.timestamp
