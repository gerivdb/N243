#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du policy_utils.py
"""

from agents.policy_utils import PolicyUtils


class TestPolicyUtils:
    def test_enforce(self):
        utils = PolicyUtils()
        report = utils.enforce(["a", "b"], {"a": True, "b": False})
        assert report.applied == ["a"]
