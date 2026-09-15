#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du concurrency_utils.py
"""

from agents.concurrency_utils import ConcurrencyUtils


class TestConcurrencyUtils:
    def test_run_tasks(self):
        utils = ConcurrencyUtils()
        results = utils.run_tasks([lambda: 1, lambda: 2])
        assert len(results) == 2
        values = [r.result for r in results]
        assert set(values) == {1, 2}

    def test_run_tasks_with_error(self):
        utils = ConcurrencyUtils()

        def bad():
            raise RuntimeError("boom")

        results = utils.run_tasks([lambda: 1, bad])
        statuses = {r.status for r in results}
        assert statuses == {"ok", "error"}
