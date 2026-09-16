#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du adapter_utils.py
"""

from agents.adapter_utils import AdapterUtils, AdapterReport


class TestAdapterUtils:
    def test_adapt(self):
        adapters = {
            "to_int": int,
            "to_str": str,
        }
        adapter = AdapterUtils(adapters)
        assert adapter.adapt("to_int", "42") == 42
        assert adapter.adapt("to_str", 42) == "42"

    def test_adapt_missing(self):
        adapter = AdapterUtils({})
        try:
            adapter.adapt("missing", 1)
            assert False, "Should have raised KeyError"
        except KeyError:
            pass

    def test_report(self):
        adapter = AdapterUtils({"to_int": int})
        report = adapter.report("to_int", "42")
        assert report.adapter_key == "to_int"
        assert report.adapted_value == 42
        assert report.timestamp
