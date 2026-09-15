#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sender_utils.py
"""

from agents.sender_utils import SenderUtils


class TestSenderUtils:
    def test_inspect(self):
        utils = SenderUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.sent == ["a"]
