#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du receiver_utils.py
"""

from agents.receiver_utils import ReceiverUtils


class TestReceiverUtils:
    def test_inspect(self):
        utils = ReceiverUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.received == ["a"]
