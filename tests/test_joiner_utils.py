#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du joiner_utils.py
"""

from agents.joiner_utils import JoinerUtils


class TestJoinerUtils:
    def test_join(self):
        utils = JoinerUtils()
        assert utils.join(["a", "b", "c"], "-") == "a-b-c"

    def test_join_empty(self):
        utils = JoinerUtils()
        assert utils.join([]) == ""

    def test_report(self):
        utils = JoinerUtils()
        report = utils.report("-", "a-b")
        assert report.result == "a-b"
