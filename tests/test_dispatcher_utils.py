#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du dispatcher_utils.py
"""

from agents.dispatcher_utils import DispatcherUtils


class TestDispatcherUtils:
    def test_distribute(self):
        utils = DispatcherUtils()
        result = utils.distribute([1, 2, 3, 4], slots=2)
        assert result[0] == [1, 3]
        assert result[1] == [2, 4]

    def test_report(self):
        utils = DispatcherUtils()
        report = utils.report([1, 2, 3, 4], slots=2)
        assert report.dispatched[0] == [1, 3]
