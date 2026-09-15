#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du composer_utils.py
"""

from agents.composer_utils import ComposerUtils


class TestComposerUtils:
    def test_compose(self):
        utils = ComposerUtils()
        assert utils.compose(["a", "b", "c"]) == "a, b, c"

    def test_report(self):
        utils = ComposerUtils()
        report = utils.report(["a", "b", "c"])
        assert report.count == 3
