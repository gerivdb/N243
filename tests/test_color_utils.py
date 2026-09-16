#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du color_utils.py
"""

from agents.color_utils import ColorUtils, ColorReport


class TestColorUtils:
    def test_hex_to_rgb(self):
        assert ColorUtils.hex_to_rgb("#FF0000") == (255, 0, 0)

    def test_rgb_to_hex(self):
        assert ColorUtils.rgb_to_hex(255, 0, 0) == "#FF0000"

    def test_roundtrip(self):
        rgb = ColorUtils.hex_to_rgb("#00FF80")
        assert ColorUtils.rgb_to_hex(*rgb) == "#00FF80"

    def test_is_hex_valid(self):
        assert ColorUtils.is_hex("#FF0000") is True
        assert ColorUtils.is_hex("FF0000") is True

    def test_is_hex_invalid(self):
        assert ColorUtils.is_hex("red") is False
        assert ColorUtils.is_hex("#FFF") is False

    def test_report(self):
        r = ColorUtils.report("#FF0000")
        assert r.hex_color == "#FF0000"
        assert r.rgb == (255, 0, 0)
        assert r.timestamp
