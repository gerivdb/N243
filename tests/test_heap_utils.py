#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du heap_utils.py
"""

from agents.heap_utils import HeapUtils


class TestHeapUtils:
    def test_min_heap(self):
        heap = HeapUtils(min_heap=True)
        heap.push(3)
        heap.push(1)
        heap.push(2)
        assert heap.pop() == 1
        assert heap.pop() == 2
        assert heap.pop() == 3

    def test_max_heap(self):
        heap = HeapUtils(min_heap=False)
        heap.push(1)
        heap.push(2)
        heap.push(3)
        assert heap.pop() == 3
        assert heap.pop() == 2
        assert heap.pop() == 1

    def test_peek(self):
        heap = HeapUtils()
        heap.push(5)
        assert heap.peek() == 5
        heap.push(1)
        assert heap.peek() == 1
