#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du queue_utils.py
"""

from agents.queue_utils import QueueUtils


class TestQueueUtils:
    def test_enqueue_and_dequeue(self):
        queue = QueueUtils()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() is None

    def test_peek(self):
        queue = QueueUtils()
        queue.enqueue(1)
        assert queue.peek() == 1
        queue.enqueue(2)
        assert queue.peek() == 1

    def test_size(self):
        queue = QueueUtils()
        assert queue.size() == 0
        queue.enqueue(1)
        assert queue.size() == 1

    def test_report(self):
        queue = QueueUtils()
        queue.enqueue(1)
        result = queue.report("enqueue", 1)
        assert result.operation == "enqueue"
        assert result.size == 1
