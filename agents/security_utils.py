#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
security_utils.py — N243 Security Utils

Rôle :
- Fournir des utilitaires de sécurité basiques
- Masquer des données sensibles
- Publier un rapport de sécurité
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class SecurityResult:
    action: str
    safe: bool
    detail: str
    timestamp: str


class SecurityUtils:
    def mask(self, value: str, visible_prefix: int = 0, visible_suffix: int = 0, mask_char: str = "*") -> str:
        if len(value) <= visible_prefix + visible_suffix:
            return mask_char * len(value)
        return value[:visible_prefix] + mask_char * (len(value) - visible_prefix - visible_suffix) + value[-visible_suffix:]

    def hash_sha256(self, value: str) -> str:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def audit(self, payload: Dict[str, Any], sensitive_keys: List[str]) -> SecurityResult:
        found = [k for k in sensitive_keys if k in payload]
        safe = len(found) == 0
        return SecurityResult(
            action="audit",
            safe=safe,
            detail=f"sensitive_keys_found={found}" if found else "clean",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
