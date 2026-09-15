#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du poller.py
"""

import time
from agents.poller import Poller


class TestPoller:
    def test_poll_success(self):
        poller = Poller(interval_sec=0.0)
        result = poller.poll("check", lambda: 42)
        assert result.success is True
        assert result.value == 42
        assert result.poll_name == "check"

    def test_poll_failure(self):
        poller = Poller(interval_sec=0.0)

        def failing():
            raise RuntimeError("fail")

        result = poller.poll("check", failing)
        assert result.success is False
        assert result.value is None

    def test_report(self):
        poller = Poller(interval_sec=0.0)
        poller.poll("a", lambda: 1)
        poller.poll("b", lambda: 2)
        report = poller.report()
        assert report["total"] == 2
        assert report["success"] == 2
