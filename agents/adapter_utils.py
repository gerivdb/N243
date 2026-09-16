#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
adapter_utils.py — N243 Adapter Utils

Rôle :
- Fournir un adaptateur simple d'interfaces
- Adapter des valeurs via des fonctions enregistrées
- Publier un rapport d'adaptation
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict


@dataclass
class AdapterReport:
    adapter_key: str
    adapted_value: Any
    timestamp: str


class AdapterUtils:
    def __init__(self, adapters: Dict[str, Callable[[Any], Any]]) -> None:
        self._adapters = adapters

    def adapt(self, key: str, value: Any) -> Any:
        func = self._adapters.get(key)
        if func is None:
            raise KeyError(key)
        return func(value)

    def report(self, key: str, value: Any) -> AdapterReport:
        adapted = self.adapt(key, value)
        return AdapterReport(
            adapter_key=key,
            adapted_value=adapted,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
