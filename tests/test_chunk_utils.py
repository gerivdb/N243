#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du chunk_utils.py
"""

from agents.chunk_utils import ChunkUtils


class TestChunkUtils:
    def test_apply(self):
        utils = ChunkUtils()
        report = utils.apply([1, 2, 3, 4, 5], size=2)
        assert report.chunks == [[1, 2], [3, 4], [5]]
