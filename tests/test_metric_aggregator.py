#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du metric_aggregator.py
"""

from agents.metric_aggregator import MetricAggregator, MetricSample


class TestMetricAggregator:
    def test_aggregate_by_name(self):
        aggregator = MetricAggregator()
        aggregator.add_sample(MetricSample("a", "cpu", 0.7, "2026-09-15T00:00:00+00:00"))
        aggregator.add_sample(MetricSample("a", "cpu", 0.8, "2026-09-15T00:00:00+00:00"))
        aggregator.add_sample(MetricSample("a", "cpu", 0.9, "2026-09-15T00:00:00+00:00"))
        result = aggregator.aggregate_by_name("cpu")
        assert result["count"] == 3
        assert result["avg"] == 0.8
        assert result["min"] == 0.7
        assert result["max"] == 0.9

    def test_aggregate_all(self):
        aggregator = MetricAggregator()
        aggregator.add_sample(MetricSample("a", "cpu", 0.7, "2026-09-15T00:00:00+00:00"))
        aggregator.add_sample(MetricSample("a", "ram", 0.8, "2026-09-15T00:00:00+00:00"))
        results = aggregator.aggregate_all()
        assert len(results) == 2
        names = {r["name"] for r in results}
        assert names == {"cpu", "ram"}

    def test_empty_aggregate(self):
        aggregator = MetricAggregator()
        result = aggregator.aggregate_by_name("cpu")
        assert result["count"] == 0
