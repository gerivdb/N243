#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du executor_utils.py
"""

from agents.executor_utils import ExecutorUtils, ExecutorReport


class TestExecutorUtils:
    def test_execute_chain(self):
        results = ExecutorUtils.execute_chain([lambda: 1, lambda: 2])
        assert results == [1, 2]

    def test_execute_until(self):
        results = ExecutorUtils.execute_until(
            lambda x: x >= 3,
            [lambda: 1, lambda: 2, lambda: 3, lambda: 4],
        )
        assert results == [1, 2, 3]

    def test_report(self):
        r = ExecutorUtils.report([lambda: 1], stop=False)
        assert r.stopped_by_predicate is False
        assert r.timestamp
