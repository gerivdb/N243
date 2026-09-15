#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assembler.py — N243 Assembler

Rôle :
- Assembler des payloads à partir de fragments
- Valider la cohérence des assemblages
- Publier un rapport d'assemblage
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class AssemblyResult:
    assembled: Dict[str, Any]
    missing_fields: List[str]
    timestamp: str


class Assembler:
    def __init__(self, required_fields: Optional[List[str]] = None) -> None:
        self.required_fields = required_fields or []

    def assemble(self, fragments: List[Dict[str, Any]]) -> AssemblyResult:
        assembled: Dict[str, Any] = {}
        for fragment in fragments:
            assembled.update(fragment)
        missing_fields = [field for field in self.required_fields if field not in assembled]
        return AssemblyResult(
            assembled=assembled,
            missing_fields=missing_fields,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def is_complete(self, fragments: List[Dict[str, Any]]) -> bool:
        result = self.assemble(fragments)
        return len(result.missing_fields) == 0
