#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du indexer_utils.py
"""

from agents.indexer_utils import IndexerUtils, IndexerReport


class TestIndexerUtils:
    def test_add_and_index(self):
        idx = IndexerUtils()
        idx.add("a")
        idx.add("b")
        result = idx.index("test")
        assert result["count"] == 2
        assert result["first"] == "a"
        assert result["last"] == "b"

    def test_all(self):
        idx = IndexerUtils()
        idx.add("a")
        idx.add("b")
        assert idx.all() == ["a", "b"]

    def test_index_empty(self):
        idx = IndexerUtils()
        result = idx.index("test")
        assert result["count"] == 0
        assert result["first"] is None
        assert result["last"] is None

    def test_report(self):
        idx = IndexerUtils()
        idx.add("x")
        r = idx.report()
        assert r.count == 1
        assert r.first == "x"
        assert r.timestamp
