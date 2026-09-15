#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du registry.py
"""

from agents.registry import Registry, RegistryEntry


class TestRegistry:
    def test_add_and_get(self):
        registry = Registry()
        entry = registry.add("key", {"a": 1})
        assert registry.get("key") == entry
        assert registry.get("missing") is None

    def test_list_names(self):
        registry = Registry()
        registry.add("a", 1)
        registry.add("b", 2)
        assert registry.list_names() == ["a", "b"]

    def test_report(self):
        registry = Registry()
        registry.add("a", 1)
        report = registry.report()
        assert report["count"] == 1
        assert report["entries"][0]["name"] == "a"
