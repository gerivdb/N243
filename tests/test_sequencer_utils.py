#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du sequencer_utils.py
"""

from agents.sequencer_utils import SequencerUtils


class TestSequencerUtils:
    def test_run_success(self):
        sequencer = SequencerUtils([lambda: 1, lambda: 2])
        reports = sequencer.run()
        assert len(reports) == 2
        assert reports[0].result == 1
        assert reports[1].result == 2

    def test_run_stops_on_error(self):
        def bad():
            raise RuntimeError("boom")

        sequencer = SequencerUtils([lambda: 1, bad, lambda: 3])
        reports = sequencer.run()
        assert len(reports) == 2
        assert reports[1].status == "error"
