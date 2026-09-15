#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du serializer_utils.py
"""

from agents.serializer_utils import SerializerUtils


class TestSerializerUtils:
    def test_to_string(self):
        utils = SerializerUtils()
        assert "a" in utils.to_string({"a": 1})

    def test_report(self):
        utils = SerializerUtils()
        report = utils.report({"a": 1})
        assert report.length > 0
