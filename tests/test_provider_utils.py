#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du provider_utils.py
"""

from agents.provider_utils import ProviderUtils


class TestProviderUtils:
    def test_inspect(self):
        utils = ProviderUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.provided == ["a"]
