#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du decorator_utils.py
"""

import time

from agents.decorator_utils import DecoratorReport, log_call, report, retry


class TestDecoratorUtils:
    def test_retry_success(self):
        call_count = {"count": 0}

        @retry(attempts=3)
        def flaky():
            call_count["count"] += 1
            if call_count["count"] < 2:
                raise RuntimeError("boom")
            return "ok"

        assert flaky() == "ok"

    def test_retry_failure(self):
        @retry(attempts=2)
        def always_fails():
            raise RuntimeError("boom")

        try:
            always_fails()
            assert False, "Should have raised RuntimeError"
        except RuntimeError:
            pass

    def test_log_call(self, capsys):
        @log_call
        def add(a, b):
            return a + b

        assert add(1, 2) == 3
        captured = capsys.readouterr()
        assert "CALL add" in captured.out

    def test_report(self):
        r = report("test_func", 3, True)
        assert r.function_name == "test_func"
        assert r.attempts == 3
        assert r.success is True
        assert r.timestamp
