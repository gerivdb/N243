#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du controller_utils.py
"""

from agents.controller_utils import ControllerUtils


class TestControllerUtils:
    def test_manage(self):
        utils = ControllerUtils()
        report = utils.manage(["a", "b"], {"a": True, "b": False})
        assert report.controlled == ["a"]
