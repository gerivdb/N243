#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
queue_processor.py — N243 Queue Processor

Rôle :
- Traiter une file d'attente d'événements/tâches
- Dédoublonner les entrées
- Publier un rapport de traitement
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional


@dataclass
class QueueItem:
    item_id: str
    payload: Dict[str, Any]
    timestamp: str


class QueueProcessor:
    def __init__(self, processor: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        self.processor = processor
        self.queue: List[QueueItem] = []
        self.results: List[Dict[str, Any]] = []

    def enqueue(self, item: QueueItem) -> None:
        self.queue.append(item)

    def process(self, deduplicate: bool = True) -> List[Dict[str, Any]]:
        seen = set()
        for item in self.queue:
            if deduplicate and item.item_id in seen:
                continue
            seen.add(item.item_id)
            result = self.processor(item.payload)
            result.setdefault("item_id", item.item_id)
            result.setdefault("timestamp", datetime.now(timezone.utc).isoformat())
            self.results.append(result)
        return self.results

    def report(self) -> Dict[str, Any]:
        return {
            "queued": len(self.queue),
            "processed": len(self.results),
            "results": self.results,
        }

    def to_json(self) -> str:
        return json.dumps(self.report(), ensure_ascii=False, indent=2)
