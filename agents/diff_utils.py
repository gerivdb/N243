#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diff_utils.py — N243 Diff Utils

Rôle :
- Comparer deux structures de données simples
- Produire un diff minimal
- Publier un rapport de diff
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class DiffResult:
    path: str
    kind: str
    old_value: Any
    new_value: Any
    timestamp: str


class DiffUtils:
    def compare(self, old: Dict[str, Any], new: Dict[str, Any], prefix: str = "") -> List[DiffResult]:
        results: List[DiffResult] = []
        all_keys = sorted(set(old) | set(new))
        for key in all_keys:
            path = f"{prefix}.{key}" if prefix else key
            in_old = key in old
            in_new = key in new
            if in_old and not in_new:
                results.append(DiffResult(path=path, kind="removed", old_value=old[key], new_value=None, timestamp=datetime.now(timezone.utc).isoformat()))
            elif not in_old and in_new:
                results.append(DiffResult(path=path, kind="added", old_value=None, new_value=new[key], timestamp=datetime.now(timezone.utc).isoformat()))
            elif old[key] != new[key]:
                results.append(DiffResult(path=path, kind="changed", old_value=old[key], new_value=new[key], timestamp=datetime.now(timezone.utc).isoformat()))
        return results

    def report(self, old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
        diffs = self.compare(old, new)
        return {
            "changed": sum(1 for d in diffs if d.kind == "changed"),
            "added": sum(1 for d in diffs if d.kind == "added"),
            "removed": sum(1 for d in diffs if d.kind == "removed"),
            "total": len(diffs),
        }
