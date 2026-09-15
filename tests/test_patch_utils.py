#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du patch_utils.py
"""

from agents.patch_utils import PatchUtils


class TestPatchUtils:
    def test_apply(self):
        utils = PatchUtils()
        report = utils.apply([1, 2, 3], index=1, replacement=9)
        assert report.patched == [1, 9, 3]
