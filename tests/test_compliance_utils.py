#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du compliance_utils.py
"""

from agents.compliance_utils import ComplianceUtils


class TestComplianceUtils:
    def test_check(self):
        utils = ComplianceUtils()
        report = utils.check(["a", "b"], {"a": True, "b": False})
        assert report.compliant == ["a"]
