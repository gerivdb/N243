#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
error_classifier.py — N243 Error Classifier

Rôle :
- Classer les erreurs par type (transient, permanent, unknown)
- Associer des stratégies de récupération
- Publier un rapport d'erreurs
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class ClassifiedError:
    error_id: str
    error_type: str
    message: str
    recovery: str
    timestamp: str


class ErrorClassifier:
    def __init__(self) -> None:
        self.errors: List[ClassifiedError] = []

    def classify(self, error_id: str, message: str) -> ClassifiedError:
        error_type = "unknown"
        recovery = "investigate"
        lower = message.lower()
        if any(token in lower for token in ["timeout", "temporary", "retry", "busy"]):
            error_type = "transient"
            recovery = "retry"
        elif any(token in lower for token in ["not found", "invalid", "forbidden", "unauthorized"]):
            error_type = "permanent"
            recovery = "abort"
        return ClassifiedError(
            error_id=error_id,
            error_type=error_type,
            message=message,
            recovery=recovery,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

    def add_error(self, error_id: str, message: str) -> ClassifiedError:
        classified = self.classify(error_id, message)
        self.errors.append(classified)
        return classified

    def report(self) -> Dict[str, Any]:
        return {
            "total": len(self.errors),
            "transient": sum(1 for e in self.errors if e.error_type == "transient"),
            "permanent": sum(1 for e in self.errors if e.error_type == "permanent"),
            "unknown": sum(1 for e in self.errors if e.error_type == "unknown"),
            "errors": [
                {
                    "error_id": e.error_id,
                    "error_type": e.error_type,
                    "message": e.message,
                    "recovery": e.recovery,
                    "timestamp": e.timestamp,
                }
                for e in self.errors
            ],
        }

    def to_json(self) -> str:
        return json.dumps(self.report(), ensure_ascii=False, indent=2)
