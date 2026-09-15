#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clusterer_utils.py — N243 Clusterer Utils

Rôle :
- Fournir un clusterer simple par seuil
- Grouper des valeurs numeriques par tranche
- Publier un rapport de clustering
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class ClusterReport:
    clusters: int
    timestamp: str


class ClustererUtils:
    @staticmethod
    def cluster(values: List[float], threshold: float = 1.0) -> Dict[int, List[float]]:
        clusters: Dict[int, List[float]] = {}
        cluster_id = 0
        current: List[float] = []
        for value in values:
            if not current or abs(value - current[-1]) <= threshold:
                current.append(value)
            else:
                clusters[cluster_id] = current
                cluster_id += 1
                current = [value]
        if current:
            clusters[cluster_id] = current
        return clusters

    def report(self, values: List[float], threshold: float = 1.0) -> ClusterReport:
        clusters = self.cluster(values, threshold)
        return ClusterReport(
            clusters=len(clusters),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
