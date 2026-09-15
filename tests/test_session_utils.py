#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du session_utils.py
"""

from agents.session_utils import SessionUtils


class TestSessionUtils:
    def test_manage(self):
        utils = SessionUtils()
        report = utils.manage(["a", "b"], {"a": True, "b": False})
        assert report.started == ["a"]
