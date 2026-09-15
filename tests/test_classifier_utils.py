#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du classifier_utils.py
"""

from agents.classifier_utils import ClassifierUtils


class TestClassifierUtils:
    def test_classify_match(self):
        rules = {
            "positive": lambda x: x > 0,
            "negative": lambda x: x < 0,
        }
        classifier = ClassifierUtils(rules)
        result = classifier.classify(5)
        assert result.label == "positive"
        assert result.score == 1.0

    def test_classify_no_match(self):
        rules = {
            "positive": lambda x: x > 0,
            "negative": lambda x: x < 0,
        }
        classifier = ClassifierUtils(rules)
        result = classifier.classify(0)
        assert result.label == "unknown"
        assert result.score == 0.0
