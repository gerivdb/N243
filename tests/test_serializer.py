#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du serializer.py
"""

from agents.serializer import Serializer


class TestSerializer:
    def test_roundtrip_json(self):
        serializer = Serializer()
        data = {"a": 1, "b": "text"}
        result = serializer.to_json(data)
        assert result.success is True
        parsed = serializer.from_json(result.data)
        assert parsed.success is True

    def test_invalid_json(self):
        serializer = Serializer()
        result = serializer.from_json("not-json")
        assert result.success is False
