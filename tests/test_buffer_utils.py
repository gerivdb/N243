#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du buffer_utils.py
"""

from agents.buffer_utils import BufferUtils


class TestBufferUtils:
    def test_add_and_drain(self):
        buffer = BufferUtils()
        buffer.add(1)
        buffer.add(2)
        assert buffer.drain() == [1, 2]

    def test_report(self):
        buffer = BufferUtils()
        buffer.add(1)
        report = buffer.report()
        assert report.size == 1
        assert report.items == [1]
