#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du batch_utils.py
"""

from agents.batch_utils import BatchUtils


class TestBatchUtils:
    def test_batch(self):
        utils = BatchUtils()
        assert utils.batch([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_batch_full(self):
        utils = BatchUtils()
        assert utils.batch([1, 2, 3], 3) == [[1, 2, 3]]

    def test_process(self):
        utils = BatchUtils()
        results = utils.process([1, 2, 3, 4], lambda batch: sum(batch), 2)
        assert len(results) == 2
        assert results[0].result == 3
        assert results[1].result == 7
