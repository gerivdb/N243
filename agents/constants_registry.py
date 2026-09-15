#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
constants_registry.py — N243 Constants Registry

Rôle :
- Centraliser les constantes métier et techniques
- Garantir la cohérence des valeurs partagées
- Publier un rapport des constantes utilisées
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Constant:
    name: str
    value: Any
    category: str


class ConstantsRegistry:
    def __init__(self) -> None:
        self.constants: Dict[str, Constant] = {}

    def register(self, constant: Constant) -> None:
        self.constants[constant.name] = constant

    def get(self, name: str) -> Optional[Constant]:
        return self.constants.get(name)

    def report(self) -> Dict[str, Any]:
        by_category: Dict[str, list] = {}
        for c in self.constants.values():
            by_category.setdefault(c.category, []).append(c.name)
        return {
            "total": len(self.constants),
            "by_category": by_category,
            "constants": [
                {
                    "name": c.name,
                    "value": c.value,
                    "category": c.category,
                }
                for c in self.constants.values()
            ],
        }

    def to_json(self) -> str:
        report = self.report()
        by_category: Dict[str, list] = {}
        for c in self.constants.values():
            by_category.setdefault(c.category, []).append(c.name)
        report["by_category"] = by_category
        return json.dumps(report, ensure_ascii=False, indent=2)
