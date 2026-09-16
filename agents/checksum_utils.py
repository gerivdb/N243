#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checksum_utils.py — N243 Checksum Utils

Rôle :
- Fournir des utilitaires de checksum simples
- Calculer md5, sha1, sha256
- Publier un rapport de checksum
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class ChecksumReport:
    text: str
    timestamp: str
    checksums: Dict[str, str] = field(default_factory=dict)


class ChecksumUtils:
    @staticmethod
    def md5(data: bytes) -> str:
        return hashlib.md5(data).hexdigest()

    @staticmethod
    def sha1(data: bytes) -> str:
        return hashlib.sha1(data).hexdigest()

    @staticmethod
    def sha256(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def checksums(text: str) -> Dict[str, str]:
        data = text.encode("utf-8")
        return {
            "md5": ChecksumUtils.md5(data),
            "sha1": ChecksumUtils.sha1(data),
            "sha256": ChecksumUtils.sha256(data),
        }

    @staticmethod
    def report(text: str) -> ChecksumReport:
        return ChecksumReport(
            text=text,
            checksums=ChecksumUtils.checksums(text),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
