#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du provider_utils.py
"""

from agents.provider_utils import ProviderUtils


class TestProviderUtils:
    def test_register_and_get(self):
        provider = ProviderUtils()
        provider.register("k", lambda: 42)
        assert provider.get("k") == 42

    def test_get_fallback(self):
        provider = ProviderUtils()
        assert provider.get("missing", 0) == 0

    def test_report(self):
        provider = ProviderUtils()
        result = provider.report("k", True, 42)
        assert result.key == "k"
        assert result.value == 42
