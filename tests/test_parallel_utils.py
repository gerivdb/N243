#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du parallel_utils.py
"""

from agents.parallel_utils import ParallelUtils


class TestParallelUtils:
    def test_run(self):
        utils = ParallelUtils()
        results = utils.run([lambda: 1, lambda: 2])
        assert len(results) == 2
        values = [r.result for r in results]
        assert set(values) == {1, 2}

    def test_run_with_error(self):
        utils = ParallelUtils()
        results = utils.run([lambda: 1, lambda: (_ for _ in ()).throw(RuntimeError("boom"))])
        statuses = {r.status for r in results}
        assert statuses == {"ok", "error"}
