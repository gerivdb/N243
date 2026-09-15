#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du model_utils.py
"""

from agents.model_utils import ModelUtils


class TestModelUtils:
    def test_verify(self):
        utils = ModelUtils()
        report = utils.verify(["a", "b"], {"a": True, "b": False})
        assert report.validated == ["a"]
