#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du resolver_utils.py
"""

from agents.resolver_utils import ResolverUtils


class TestResolverUtils:
    def test_resolve_override(self):
        assert ResolverUtils.resolve(1, 2, "override") == 2

    def test_resolve_keep(self):
        assert ResolverUtils.resolve(1, 2, "keep") == 1

    def test_resolve_merge(self):
        base = {"a": 1}
        override = {"b": 2}
        assert ResolverUtils.resolve(base, override, "merge") == {"a": 1, "b": 2}

    def test_report(self):
        utils = ResolverUtils()
        result = utils.report("key", "override", 42)
        assert result.key == "key"
        assert result.value == 42
