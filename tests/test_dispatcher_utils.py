#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du dispatcher_utils.py
"""

from agents.dispatcher_utils import DispatcherUtils


class TestDispatcherUtils:
    def test_inspect(self):
        utils = DispatcherUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.dispatched == ["a"]
