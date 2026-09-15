#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du bag_utils.py
"""

from agents.bag_utils import BagUtils


class TestBagUtils:
    def test_add_and_count(self):
        bag = BagUtils()
        bag.add("a")
        bag.add("a", 2)
        assert bag.count("a") == 3

    def test_remove(self):
        bag = BagUtils()
        bag.add("a", 3)
        bag.remove("a", 2)
        assert bag.count("a") == 1

    def test_report(self):
        bag = BagUtils()
        bag.add("a", 2)
        bag.add("b", 1)
        report = bag.report()
        assert report["unique_items"] == 2
        assert report["total_count"] == 3
