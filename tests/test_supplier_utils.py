#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du supplier_utils.py
"""

from agents.supplier_utils import SupplierUtils


class TestSupplierUtils:
    def test_register_and_get(self):
        supplier = SupplierUtils()
        supplier.register("k", lambda: 42)
        assert supplier.get("k") == 42

    def test_cache(self):
        supplier = SupplierUtils()
        supplier.register("k", lambda: 42)
        supplier.get("k")
        supplier.register("k", lambda: 99)
        assert supplier.get("k") == 42

    def test_get_fallback(self):
        supplier = SupplierUtils()
        assert supplier.get("missing", 0) == 0

    def test_report(self):
        supplier = SupplierUtils()
        result = supplier.report("k", True, 42)
        assert result.key == "k"
        assert result.value == 42
