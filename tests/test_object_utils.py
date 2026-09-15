#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du object_utils.py
"""

from agents.object_utils import ObjectUtils


class TestObjectUtils:
    def test_get(self):
        utils = ObjectUtils()
        data = {"a": {"b": 1}}
        assert utils.get(data, "a.b") == 1
        assert utils.get(data, "x.y") is None

    def test_set(self):
        utils = ObjectUtils()
        data = {"a": {}}
        utils.set(data, "a.b", 2)
        assert data == {"a": {"b": 2}}
