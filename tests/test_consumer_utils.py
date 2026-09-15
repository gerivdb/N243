#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du consumer_utils.py
"""

from agents.consumer_utils import ConsumerUtils


class TestConsumerUtils:
    def test_subscribe_and_consume(self):
        consumer = ConsumerUtils()
        seen: list = []
        consumer.subscribe("topic", seen.append)
        consumer.consume("topic", 1)
        assert seen == [1]

    def test_report(self):
        consumer = ConsumerUtils()
        result = consumer.report("topic", True, 1)
        assert result.topic == "topic"
        assert result.payload == 1
