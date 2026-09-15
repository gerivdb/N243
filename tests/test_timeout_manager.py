#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du timeout_manager.py
"""

import time
import pytest
from agents.timeout_manager import TimeoutManager


class TestTimeoutManager:
    def test_execute_within_timeout(self):
        manager = TimeoutManager()
        result = manager.execute_with_timeout("fast", lambda: 42, timeout_sec=5.0)
        assert result.timed_out is False
        assert result.elapsed_sec < 5.0

    def test_execute_timeout(self):
        manager = TimeoutManager()

        def failing():
            raise RuntimeError("operation failed")

        result = manager.execute_with_timeout("failing", failing, timeout_sec=5.0)
        assert result.timed_out is True
        assert result.elapsed_sec < 5.0

    def test_report(self):
        manager = TimeoutManager()
        manager.execute_with_timeout("fast", lambda: 42, timeout_sec=5.0)
        report = manager.report()
        assert report["total"] == 1
        assert report["timed_out"] == 0
