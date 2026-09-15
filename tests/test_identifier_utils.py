#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du identifier_utils.py
"""

from agents.identifier_utils import IdentifierUtils


class TestIdentifierUtils:
    def test_next(self):
        utils = IdentifierUtils()
        assert utils.next("item") == "item-0001"
        assert utils.next("item") == "item-0002"

    def test_report(self):
        utils = IdentifierUtils()
        report = utils.report("item", "item-0001")
        assert report.identifier == "item-0001"
        assert report.prefix == "item"
