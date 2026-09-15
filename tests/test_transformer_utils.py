#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du transformer_utils.py
"""

from agents.transformer_utils import TransformerUtils


class TestTransformerUtils:
    def test_transform(self):
        utils = TransformerUtils()
        assert utils.transform([1, 2, 3], lambda x: x * 2) == [2, 4, 6]

    def test_report(self):
        utils = TransformerUtils()
        report = utils.report([1, 2, 3])
        assert report.transformed == 3
        assert report.items == [1, 2, 3]
