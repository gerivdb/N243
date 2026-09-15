#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du cycle_stats_collector.py
"""

from agents.cycle_stats_collector import CycleStatsCollector, CycleRecord


class TestCycleStatsCollector:
    def test_empty_summary(self):
        collector = CycleStatsCollector()
        summary = collector.summary()
        assert summary["count"] == 0
        assert summary["avg_duration_sec"] == 0.0

    def test_summary_with_records(self):
        collector = CycleStatsCollector()
        for i in range(5):
            collector.add_cycle(CycleRecord(
                cycle_id=f"c{i}",
                duration_sec=10.0 + i,
                events_success=8,
                events_total=10,
                curx_score=0.9,
                timestamp="2026-09-15T00:00:00+00:00",
            ))
        summary = collector.summary()
        assert summary["count"] == 5
        assert summary["avg_duration_sec"] == 12.0
        assert summary["min_duration_sec"] == 10.0
        assert summary["max_duration_sec"] == 14.0
        assert summary["avg_success_rate"] == 0.8
        assert summary["avg_curx_score"] == 0.9

    def test_to_json(self):
        collector = CycleStatsCollector()
        collector.add_cycle(CycleRecord(
            cycle_id="c1",
            duration_sec=10.0,
            events_success=10,
            events_total=10,
            curx_score=1.0,
            timestamp="2026-09-15T00:00:00+00:00",
        ))
        output = collector.to_json()
        assert '"count": 1' in output
        assert '"avg_duration_sec": 10.0' in output
