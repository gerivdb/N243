#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du iterator_utils.py
"""

from agents.iterator_utils import IteratorUtils


class TestIteratorUtils:
    def test_paginate(self):
        utils = IteratorUtils()
        assert utils.paginate([1, 2, 3, 4, 5], 1, 2) == [1, 2]
        assert utils.paginate([1, 2, 3, 4, 5], 2, 2) == [3, 4]

    def test_report(self):
        utils = IteratorUtils()
        report = utils.report(1, 2, [1, 2])
        assert report.page == 1
        assert report.size == 2
