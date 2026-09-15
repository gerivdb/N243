#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du stream_utils.py
"""

from agents.stream_utils import StreamUtils


class TestStreamUtils:
    def test_chunk_items(self):
        utils = StreamUtils()
        chunks = utils.chunk_items([1, 2, 3, 4, 5], 2)
        assert chunks == [[1, 2], [3, 4], [5]]

    def test_chunk_items_full(self):
        utils = StreamUtils()
        chunks = utils.chunk_items([1, 2, 3], 3)
        assert chunks == [[1, 2, 3]]

    def test_consume(self):
        utils = StreamUtils()
        seen: list = []
        utils.consume([1, 2, 3], seen.append)
        assert seen == [1, 2, 3]

    def test_report(self):
        utils = StreamUtils()
        result = utils.report("chunk", 1, 10)
        assert result.chunk_index == 1
        assert result.chunk_size == 10
