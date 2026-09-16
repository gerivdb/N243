#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du net_utils.py
"""

from agents.net_utils import NetUtils, NetReport


class TestNetUtils:
    def test_parse(self):
        result = NetUtils.parse("https://example.com/path?q=1")
        assert result["scheme"] == "https"
        assert result["netloc"] == "example.com"
        assert result["path"] == "/path"

    def test_add_query(self):
        result = NetUtils.add_query("https://example.com", {"key": "value"})
        assert "key=value" in result

    def test_base(self):
        assert NetUtils.base("https://example.com/path") == "https://example.com"

    def test_report(self):
        r = NetUtils.report("https://example.com", "base")
        assert r.url == "https://example.com"
        assert r.timestamp
