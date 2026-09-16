#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
color_utils.py — N243 Color Utils

Rôle :
- Fournir une manipulation simple de couleurs hex/rgb
- Convertir hex↔rgb, valider les codes hexadécimaux
- Publier un rapport de couleur
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Tuple


@dataclass
class ColorReport:
    hex_color: str
    rgb: Tuple[int, int, int]
    timestamp: str


class ColorUtils:
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        hex_color = hex_color.lstrip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        return f"#{r:02X}{g:02X}{b:02X}"

    @staticmethod
    def is_hex(hex_color: str) -> bool:
        hex_color = hex_color.lstrip("#")
        if len(hex_color) != 6:
            return False
        try:
            int(hex_color, 16)
            return True
        except ValueError:
            return False

    @staticmethod
    def report(hex_color: str) -> ColorReport:
        rgb = ColorUtils.hex_to_rgb(hex_color) if ColorUtils.is_hex(hex_color) else (0, 0, 0)
        return ColorReport(
            hex_color=hex_color,
            rgb=rgb,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
