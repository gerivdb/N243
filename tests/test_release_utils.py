#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du release_utils.py
"""

from agents.release_utils import ReleaseUtils


class TestReleaseUtils:
    def test_below(self):
        utils = ReleaseUtils()
        report = utils.below([1.0, 5.0, 3.0], threshold=3.0)
        assert report.released == [1.0]
