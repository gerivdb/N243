#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du reservoir_utils.py
"""

from agents.reservoir_utils import ReservoirUtils


class TestReservoirUtils:
    def test_add_and_take(self):
        reservoir = ReservoirUtils()
        assert reservoir.add(1) is True
        assert reservoir.take() == 1

    def test_capacity(self):
        reservoir = ReservoirUtils(capacity=1)
        assert reservoir.add(1) is True
        assert reservoir.add(2) is False

    def test_report(self):
        reservoir = ReservoirUtils()
        reservoir.add(1)
        report = reservoir.report()
        assert report.count == 1
        assert report.items == [1]
