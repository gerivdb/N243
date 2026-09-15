#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du annotation_utils.py
"""

from agents.annotation_utils import AnnotationUtils


class TestAnnotationUtils:
    def test_annotate_and_get(self):
        ann = AnnotationUtils()
        ann.annotate("item1", "color", "red")
        assert ann.get("item1", "color") == "red"

    def test_get_missing(self):
        ann = AnnotationUtils()
        assert ann.get("missing", "color", "default") == "default"

    def test_remove(self):
        ann = AnnotationUtils()
        ann.annotate("item1", "color", "red")
        ann.remove("item1", "color")
        assert ann.get("item1", "color") is None

    def test_keys(self):
        ann = AnnotationUtils()
        ann.annotate("item1", "color", "red")
        ann.annotate("item1", "size", "large")
        assert set(ann.keys("item1")) == {"color", "size"}

    def test_report(self):
        ann = AnnotationUtils()
        ann.annotate("item1", "color", "red")
        result = ann.report("item1", "color", "red")
        assert result.target == "item1"
        assert result.key == "color"
