#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du service_utils.py
"""

from agents.service_utils import ServiceUtils


class TestServiceUtils:
    def test_start(self):
        utils = ServiceUtils()
        report = utils.start(["api", "worker"], {"api": True, "worker": False})
        assert report.started == ["api"]
