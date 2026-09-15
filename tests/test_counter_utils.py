#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du counter_utils.py
"""

from agents.counter_utils import CounterUtils


class TestCounterUtils:
    def test_inc(self):
        counter = CounterUtils()
        assert counter.inc() == 1

    def test_dec(self):
        counter = CounterUtils()
        counter.inc()
        assert counter.dec() == 0

    def test_reset(self):
        counter = CounterUtils()
        counter.inc()
        counter.reset(5)
        assert counter.value() == 5

    def test_max_value(self):
        counter = CounterUtils(max_value=10)
        counter.inc(20)
        assert counter.value() == 10

    def test_min_value(self):
        counter = CounterUtils(min_value=0)
        counter.dec(5)
        assert counter.value() == 0
