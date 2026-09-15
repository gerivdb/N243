#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du refresher_utils.py
"""

from agents.refresher_utils import RefresherUtils


class TestRefresherUtils:
    def test_set_and_get(self):
        refresher = RefresherUtils()
        refresher.set("k", 1)
        assert refresher.get("k") == 1

    def test_refresh(self):
        refresher = RefresherUtils()
        refresher.set("k", 1)
        new_value = refresher.refresh("k", lambda: 2)
        assert new_value == 2
        assert refresher.get("k") == 2

    def test_report(self):
        refresher = RefresherUtils()
        result = refresher.report("k", 1, 2)
        assert result.target == "k"
        assert result.previous == 1
        assert result.current == 2
