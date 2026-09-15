#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du queue_processor.py
"""

from agents.queue_processor import QueueProcessor, QueueItem


class TestQueueProcessor:
    def test_process_queue(self):
        def processor(payload):
            return {"status": "ok", "value": payload.get("value", 0) * 2}

        queue = QueueProcessor(processor)
        queue.enqueue(QueueItem("1", {"value": 1}, "2026-09-15T00:00:00+00:00"))
        queue.enqueue(QueueItem("2", {"value": 2}, "2026-09-15T00:00:00+00:00"))
        results = queue.process()
        assert len(results) == 2
        assert results[0]["value"] == 2
        assert results[1]["value"] == 4

    def test_deduplicate(self):
        def processor(payload):
            return {"status": "ok", "value": payload.get("value", 0)}

        queue = QueueProcessor(processor)
        queue.enqueue(QueueItem("1", {"value": 1}, "2026-09-15T00:00:00+00:00"))
        queue.enqueue(QueueItem("1", {"value": 2}, "2026-09-15T00:00:00+00:00"))
        results = queue.process(deduplicate=True)
        assert len(results) == 1
        assert results[0]["value"] == 1
