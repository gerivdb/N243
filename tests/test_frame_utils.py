#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du frame_utils.py
"""

from agents.frame_utils import FrameUtils


class TestFrameUtils:
    def test_chunk(self):
        utils = FrameUtils()
        frames = utils.chunk([1, 2, 3, 4, 5], size=2)
        assert len(frames) == 3
        assert frames[0] == [1, 2]

    def test_report(self):
        utils = FrameUtils()
        report = utils.report([1, 2, 3, 4, 5], size=2)
        assert report.frames == 3
