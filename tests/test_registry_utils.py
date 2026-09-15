#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du registry_utils.py
"""

from agents.registry_utils import RegistryUtils


class TestRegistryUtils:
    def test_add_and_get(self):
        registry = RegistryUtils()
        registry.add("foo", 42)
        assert registry.get("foo") == 42

    def test_get_missing(self):
        registry = RegistryUtils()
        assert registry.get("missing", "default") == "default"

    def test_remove(self):
        registry = RegistryUtils()
        registry.add("foo", 1)
        registry.remove("foo")
        assert registry.has("foo") is False

    def test_list_items(self):
        registry = RegistryUtils()
        registry.add("a", 1)
        registry.add("b", 2)
        assert set(registry.list_items()) == {"a", "b"}

    def test_report(self):
        registry = RegistryUtils()
        result = registry.report("add", "foo", "ok")
        assert result.operation == "add"
        assert result.status == "ok"
