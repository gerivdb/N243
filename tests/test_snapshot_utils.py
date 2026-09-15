#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du snapshot_utils.py
"""

from agents.snapshot_utils import SnapshotUtils


class TestSnapshotUtils:
    def test_capture(self):
        utils = SnapshotUtils()
        report = utils.capture(["a", "b"], {"a": 1, "b": None})
        assert report.captured == ["a"]
