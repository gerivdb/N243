#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du predictor_utils.py
"""

from agents.predictor_utils import PredictorUtils


class TestPredictorUtils:
    def test_predict(self):
        utils = PredictorUtils()
        assert utils.predict([1.0, 2.0, 3.0]) == 3.0

    def test_report(self):
        utils = PredictorUtils()
        report = utils.report([1.0, 2.0, 3.0])
        assert report.last == 3.0
        assert report.next == 3.0
