#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du worker_utils.py
"""

from agents.worker_utils import WorkerUtils


class TestWorkerUtils:
    def test_process(self):
        worker = WorkerUtils(lambda x: x * 2)
        results = worker.process([1, 2, 3])
        assert [r.result for r in results] == [2, 4, 6]

    def test_process_with_error(self):
        def bad(x):
            if x == 2:
                raise RuntimeError("boom")
            return x

        worker = WorkerUtils(bad)
        results = worker.process([1, 2, 3])
        assert results[0].status == "ok"
        assert results[1].status == "error"
        assert results[2].status == "ok"
