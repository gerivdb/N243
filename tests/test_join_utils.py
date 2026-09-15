#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du join_utils.py
"""

from agents.join_utils import JoinUtils


class TestJoinUtils:
    def test_apply(self):
        utils = JoinUtils()
        report = utils.apply([1, 2], [2, 3])
        assert report.joined == [1, 2, 3]
