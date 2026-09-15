#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du decomposer_utils.py
"""

from agents.decomposer_utils import DecomposerUtils


class TestDecomposerUtils:
    def test_decompose(self):
        utils = DecomposerUtils()
        assert utils.decompose("a, b, c") == ["a", "b", "c"]

    def test_report(self):
        utils = DecomposerUtils()
        report = utils.report(["a", "b", "c"])
        assert report.count == 3
