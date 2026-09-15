#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du unique_utils.py
"""

from agents.unique_utils import UniqueUtils


class TestUniqueUtils:
    def test_apply(self):
        utils = UniqueUtils()
        report = utils.apply([1, 2, 2, 3])
        assert report.unique == [1, 2, 3]
