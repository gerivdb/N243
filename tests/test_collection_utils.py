#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du collection_utils.py
"""

from agents.collection_utils import CollectionUtils


class TestCollectionUtils:
    def test_deduplicate(self):
        utils = CollectionUtils()
        items = [1, 2, 2, 3, 3, 3]
        result = utils.deduplicate(items)
        assert result == [1, 2, 3]

    def test_partition(self):
        utils = CollectionUtils()
        items = [1, 2, 3, 4]
        matched, unmatched = utils.partition(items, lambda x: x % 2 == 0)
        assert matched == [2, 4]
        assert unmatched == [1, 3]

    def test_report(self):
        utils = CollectionUtils()
        report = utils.report("dedup", 10, 5)
        assert report.operation == "dedup"
        assert report.input_count == 10
        assert report.output_count == 5
