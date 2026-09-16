#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gateway_utils.py — N243 Gateway Utils

Rôle :
- Fournir un outil de passerelle simple
- Publier un rapport de passerelle
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class GatewayReport:
    routed: List[str]
    timestamp: str


class GatewayUtils:
    @staticmethod
    def inspect(gateways: List[str], payload: Dict[str, Any]) -> GatewayReport:
        routed = [gateway for gateway in gateways if payload.get(gateway) is True]
        return GatewayReport(
            routed=routed,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
