#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du audit_utils.py
"""

from agents.audit_utils import AuditUtils


class TestAuditUtils:
    def test_review(self):
        utils = AuditUtils()
        report = utils.review(["a", "b"], {"a": 1, "b": None})
        assert report.audited == ["a"]
