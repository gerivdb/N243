#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du handler_utils.py
"""

from agents.handler_utils import HandlerUtils


class TestHandlerUtils:
    def test_dispatch(self):
        utils = HandlerUtils()
        report = utils.dispatch(["a", "b"], {"a": 1})
        assert report.handled == ["a"]
        assert report.skipped == ["b"]
