#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du security_utils.py
"""

from agents.security_utils import SecurityUtils


class TestSecurityUtils:
    def test_mask(self):
        utils = SecurityUtils()
        assert utils.mask("1234567890", visible_prefix=2, visible_suffix=1) == "12*******0"

    def test_hash_sha256(self):
        utils = SecurityUtils()
        digest = utils.hash_sha256("secret")
        assert len(digest) == 64

    def test_audit_clean(self):
        utils = SecurityUtils()
        result = utils.audit({"a": 1}, ["password", "token"])
        assert result.safe is True
        assert result.detail == "clean"

    def test_audit_sensitive(self):
        utils = SecurityUtils()
        result = utils.audit({"password": "x"}, ["password", "token"])
        assert result.safe is False
        assert "password" in result.detail
