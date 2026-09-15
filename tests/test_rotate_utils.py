#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du rotate_utils.py
"""

from agents.rotate_utils import RotateUtils


class TestRotateUtils:
    def test_apply(self):
        utils = RotateUtils()
        report = utils.apply([1, 2, 3], steps=1)
        assert report.rotated == [3, 1, 2]
