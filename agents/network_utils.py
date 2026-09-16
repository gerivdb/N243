#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
network_utils.py — N24 N243 Network Utils

Rôle :
- Fournir un outil simple de gestion réseau
- Publier un rapport de connexions traitées
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List


@dataclass
class NetworkReport:
    connections: List[str]
    timestamp: str


class NetworkUtils:
    @staticmethod
    def inspect(connections: List[str]) -> NetworkReport:
        return NetworkReport(
            connections=list(connections),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
