#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du schema_utils.py
"""

from agents.schema_utils import SchemaUtils


class TestSchemaUtils:
    def test_inspect(self):
        utils = SchemaUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.valid == ["a"]
