#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du deserializer_utils.py
"""

from agents.deserializer_utils import DeserializerUtils


class TestDeserializerUtils:
    def test_from_string(self):
        utils = DeserializerUtils()
        assert utils.from_string("{'a': 1}") == {"a": 1}

    def test_report(self):
        utils = DeserializerUtils()
        report = utils.report(True)
        assert report.success is True
