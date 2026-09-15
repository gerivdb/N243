#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du collection_utils.py
"""

from agents.collection_utils import CollectionUtils


class TestCollectionUtils:
    def test_group_by(self):
        utils = CollectionUtils()
        items = [{"type": "a", "v": 1}, {"type": "b", "v": 2}, {"type": "a", "v": 3}]
        grouped = utils.group_by(items, lambda x: x["type"])
        assert grouped["a"] == [{"type": "a", "v": 1}, {"type": "a", "v": 3}]

    def test_count_by(self):
        utils = CollectionUtils()
        items = [1, 2, 2, 3, 3, 3]
        counts = utils.count_by(items, lambda x: x)
        assert counts[3] == 3

    def test_flatten(self):
        utils = CollectionUtils()
        assert utils.flatten([[1, 2], [3]]) == [1, 2, 3]

    def test_report(self):
        utils = CollectionUtils()
        result = utils.report("flatten", 2, 3, [1, 2, 3])
        assert result.operation == "flatten"
        assert result.output_count == 3
