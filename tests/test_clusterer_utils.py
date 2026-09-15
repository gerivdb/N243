#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du clusterer_utils.py
"""

from agents.clusterer_utils import ClustererUtils


class TestClustererUtils:
    def test_cluster(self):
        utils = ClustererUtils()
        clusters = utils.cluster([1.0, 1.1, 2.5, 2.6, 2.7], threshold=0.5)
        assert len(clusters) == 2

    def test_report(self):
        utils = ClustererUtils()
        report = utils.report([1.0, 1.1, 2.5, 2.6, 2.7], threshold=0.5)
        assert report.clusters == 2
