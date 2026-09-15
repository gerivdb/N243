#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sanitizer.py
"""

import json
from agents.sanitizer import Sanitizer, SanitizationResult


class TestSanitizer:
    def test_sanitize_masks_fields(self):
        sanitizer = Sanitizer(["password", "token"])
        result = sanitizer.sanitize({"user": "admin", "password": "secret", "token": "abc"})
        assert result.sanitized["password"] == "***"
        assert result.sanitized["token"] == "***"
        assert result.sanitized["user"] == "admin"
        assert result.masked_fields == ["password", "token"]

    def test_sanitize_json(self):
        sanitizer = Sanitizer(["secret"])
        payload = json.dumps({"secret": "value", "public": 1})
        cleaned = sanitizer.sanitize_json(payload)
        assert json.loads(cleaned)["secret"] == "***"
        assert json.loads(cleaned)["public"] == 1
