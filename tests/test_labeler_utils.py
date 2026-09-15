#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du labeler_utils.py
"""

from agents.labeler_utils import LabelerUtils


class TestLabelerUtils:
    def test_label(self):
        labeler = LabelerUtils()
        labeler.label("item", "red")
        assert labeler.labels_for("item") == ["red"]

    def test_multiple_labels(self):
        labeler = LabelerUtils()
        labeler.label("item", "red")
        labeler.label("item", "big")
        assert labeler.labels_for("item") == ["red", "big"]

    def test_report(self):
        labeler = LabelerUtils()
        labeler.label("item", "red")
        report = labeler.report()
        assert report.labeled == 1
        assert report.labels == ["red"]
