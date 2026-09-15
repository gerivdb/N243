#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du indexer.py
"""

from agents.indexer import Indexer


class TestIndexer:
    def test_index_and_search(self):
        indexer = Indexer()
        indexer.index_item("tag", "item-1")
        indexer.index_item("tag", "item-2")
        assert indexer.search("tag") == ["item-1", "item-2"]
        assert indexer.search("missing") == []

    def test_report(self):
        indexer = Indexer()
        indexer.index_item("a", 1)
        indexer.index_item("b", 2)
        indexer.index_item("a", 3)
        report = indexer.report()
        assert report["keys"] == 2
        assert report["items"] == 3
        assert report["index"]["a"] == 2
