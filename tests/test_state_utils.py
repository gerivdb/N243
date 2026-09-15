#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du state_utils.py
"""

from agents.state_utils import StateUtils


class TestStateUtils:
    def test_update(self):
        utils = StateUtils()
        report = utils.update({"active": False}, "active", True)
        assert report.state["active"] is True
