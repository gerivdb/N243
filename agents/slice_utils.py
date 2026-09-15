#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slice_utils.py — N243 Slice Utils

Rôle :
- Fournir des utilitaires de slicing/plage
- Découper des listes, strings, bytes
- Publier un rapport simple
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class SliceResult:
    source_type: str
    slice_obj: slice
    result: Any
    timestamp: str


class SliceUtils:
    def slice_list(self, items: List[Any], start: Optional[int] = None, stop: Optional[int] = None, step: Optional[int] = None) -> List[Any]:
        return items[slice(start, stop, step)]

    def slice_str(self, text: str, start: Optional[int] = None, stop: Optional[int] = None, step: Optional[int] = None) -> str:
        return text[slice(start, stop, step)]

    def report(self, source_type: str, slice_obj: slice, result: Any) -> SliceResult:
        return SliceResult(
            source_type=source_type,
            slice_obj=slice_obj,
            result=result,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
