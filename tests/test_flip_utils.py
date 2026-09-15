#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du flip_utils.py
"""

from agents.flip_utils import FlipUtils


class TestFlipUtils:
    def test_apply(self):
        utils = FlipUtils()
        report = utils.apply([1, 2, 3])
        assert report.flipped == [3, 2, 1]
