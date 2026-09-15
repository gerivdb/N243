#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du cache_utils.py
"""

from agents.cache_utils import CacheUtils


class TestCacheUtils:
    def test_put_and_get(self):
        cache = CacheUtils()
        cache.put("k", 42)
        assert cache.get("k") == 42

    def test_get_missing(self):
        cache = CacheUtils()
        assert cache.get("missing", "default") == "default"

    def test_invalidate(self):
        cache = CacheUtils()
        cache.put("k", 1)
        cache.invalidate("k")
        assert cache.get("k") is None

    def test_keys(self):
        cache = CacheUtils()
        cache.put("a", 1)
        cache.put("b", 2)
        assert set(cache.keys()) == {"a", "b"}

    def test_report(self):
        cache = CacheUtils()
        cache.put("k", 1)
        result = cache.report("get", "k", True)
        assert result.key == "k"
        assert result.hit is True
