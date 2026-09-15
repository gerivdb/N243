#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du error_classifier.py
"""

from agents.error_classifier import ErrorClassifier


class TestErrorClassifier:
    def test_classify_transient(self):
        classifier = ErrorClassifier()
        error = classifier.add_error("e1", "Connection timeout")
        assert error.error_type == "transient"
        assert error.recovery == "retry"

    def test_classify_permanent(self):
        classifier = ErrorClassifier()
        error = classifier.add_error("e2", "Resource not found")
        assert error.error_type == "permanent"
        assert error.recovery == "abort"

    def test_classify_unknown(self):
        classifier = ErrorClassifier()
        error = classifier.add_error("e3", "Unexpected failure")
        assert error.error_type == "unknown"
        assert error.recovery == "investigate"

    def test_report(self):
        classifier = ErrorClassifier()
        classifier.add_error("e1", "Connection timeout")
        classifier.add_error("e2", "Resource not found")
        report = classifier.report()
        assert report["total"] == 2
        assert report["transient"] == 1
        assert report["permanent"] == 1
