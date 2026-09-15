#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du clip_utils.py
"""

from agents.clip_utils import ClipUtils


class TestClipUtils:
    def test_apply(self):
        utils = ClipUtils()
        report = utils.apply([1, 2, 3, 4, 5], minimum=2, maximum=4)
        assert report.clipped == [2, 2, 3, 4, 4]
