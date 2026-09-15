#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du rule_utils.py
"""

from agents.rule_utils import RuleUtils


class TestRuleUtils:
    def test_evaluate(self):
        utils = RuleUtils()
        report = utils.evaluate(["a", "b"], {"a": True, "b": False})
        assert report.matched == ["a"]
