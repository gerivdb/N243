#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du constants_registry.py
"""

from agents.constants_registry import ConstantsRegistry, Constant


class TestConstantsRegistry:
    def test_register_and_get(self):
        registry = ConstantsRegistry()
        registry.register(Constant("MAX_RETRIES", 3, "general"))
        constant = registry.get("MAX_RETRIES")
        assert constant is not None
        assert constant.value == 3
        assert constant.category == "general"

    def test_report(self):
        registry = ConstantsRegistry()
        registry.register(Constant("MAX_RETRIES", 3, "general"))
        registry.register(Constant("TIMEOUT", 30, "general"))
        registry.register(Constant("BATCH_SIZE", 100, "batch"))
        report = registry.report()
        assert report["total"] == 3
        assert report["by_category"]["general"] == ["MAX_RETRIES", "TIMEOUT"]
        assert report["by_category"]["batch"] == ["BATCH_SIZE"]
