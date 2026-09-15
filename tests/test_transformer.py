#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du transformer.py
"""

from agents.transformer import Transformer


class TestTransformer:
    def test_apply(self):
        transformer = Transformer()
        result = transformer.apply(2, "double", lambda x: x * 2)
        assert result == 4
        report = transformer.report()
        assert report["total"] == 1

    def test_multiple_transforms(self):
        transformer = Transformer()
        transformer.apply(1, "inc", lambda x: x + 1)
        transformer.apply(2, "double", lambda x: x * 2)
        report = transformer.report()
        assert report["total"] == 2
