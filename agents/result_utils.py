#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
result_utils.py — N243 Result Utils

Rôle :
- Fournir un conteneur de résultat standardisé
- Encapsuler succès/échec, valeur, erreur
- Publier un rapport lisible
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Result(Generic[T]):
    success: bool
    value: Optional[T]
    error: Optional[str]
    timestamp: str


class ResultUtils:
    @staticmethod
    def ok(value: T) -> Result[T]:
        return Result(
            success=True,
            value=value,
            error=None,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    @staticmethod
    def fail(error: str) -> Result[None]:
        return Result(
            success=False,
            value=None,
            error=error,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
