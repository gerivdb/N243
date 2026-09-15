#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du deduplicator_utils.py
"""

from agents.deduplicator_utils import DeduplicatorUtils


class TestDeduplicatorUtils:
    def test_deduplicate(self):
        utils = DeduplicatorUtils()
        assert utils.deduplicate([1, 2, 1, 3, 2]) == [1, 2, 3]

    def test_deduplicate_preserve_order(self):
        utils = DeduplicatorUtils()
        assert utils.deduplicate([3, 1, 2, 1, 3]) == [3, 1, 2]

    def test_report(self):
        utils = DeduplicatorUtils()
        result = utils.report([1, 1, 2])
        assert result.input_count == 3
        assert result.output_count == 2
        assert result.output == [1, 2]
