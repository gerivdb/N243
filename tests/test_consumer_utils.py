#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du consumer_utils.py
"""

from agents.consumer_utils import ConsumerUtils


class TestConsumerUtils:
    def test_inspect(self):
        utils = ConsumerUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.consumed == ["a"]
