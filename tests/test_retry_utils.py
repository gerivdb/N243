#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du retry_utils.py
"""

from agents.retry_utils import RetryUtils


class TestRetryUtils:
    def test_success_first_attempt(self):
        utils = RetryUtils()
        report = utils.run(lambda: 42, attempts=3)
        assert report.success is True
        assert report.value == 42
        assert report.attempt == 1

    def test_success_after_retry(self):
        utils = RetryUtils()
        calls = {"count": 0}

        def flaky():
            calls["count"] += 1
            if calls["count"] < 3:
                raise RuntimeError("boom")
            return "ok"

        report = utils.run(flaky, attempts=5)
        assert report.success is True
        assert report.value == "ok"
        assert report.attempt == 3

    def test_failure_after_exhausted(self):
        utils = RetryUtils()
        report = utils.run(lambda: (_ for _ in ()).throw(RuntimeError("boom")), attempts=2)
        assert report.success is False
        assert report.error == "boom"
