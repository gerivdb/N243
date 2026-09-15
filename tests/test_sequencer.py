#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sequencer.py
"""

from agents.sequencer import Sequencer


class TestSequencer:
    def test_run_step_success(self):
        sequencer = Sequencer()
        result = sequencer.run_step("step-1", lambda: 42)
        assert result.success is True
        assert result.result == 42

    def test_run_step_failure(self):
        sequencer = Sequencer()

        def failing():
            raise RuntimeError("fail")

        result = sequencer.run_step("step-1", failing)
        assert result.success is False
        assert "fail" in result.result

    def test_run_sequence(self):
        sequencer = Sequencer()
        results = sequencer.run_sequence([
            ("step-1", lambda: 1),
            ("step-2", lambda: 2),
        ])
        assert len(results) == 2
        assert all(r.success for r in results)
        report = sequencer.report()
        assert report["total_steps"] == 2
        assert report["success"] == 2
