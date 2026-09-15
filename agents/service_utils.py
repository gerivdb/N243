#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
service_utils.py — N243 Service Utils

Rôle :
- Fournir un service simple
- Publier un rapport de service
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ServiceReport:
    started: List[str]
    timestamp: str


class ServiceUtils:
    @staticmethod
    def start(services: List[str], payload: Dict[str, Any]) -> ServiceReport:
        started = [service for service in services if payload.get(service)]
        return ServiceReport(
            started=started,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
