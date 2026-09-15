#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parser_utils.py — N243 Parser Utils

Rôle :
- Fournir un parseur simple de texte
- Extraire des champs d'une ligne délimitée
- Publier un rapport de parsing
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ParseReport:
    fields: int
    timestamp: str


class ParserUtils:
    @staticmethod
    def parse_line(line: str, delimiter: str = ",") -> Dict[str, str]:
        parts = line.split(delimiter)
        return {f"field_{i}": part for i, part in enumerate(parts)}

    def report(self, fields: Dict[str, str]) -> ParseReport:
        return ParseReport(
            fields=len(fields),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
