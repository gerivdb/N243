#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du traverser_utils.py
"""

from agents.traverser_utils import TraverserUtils


class TestTraverserUtils:
    def test_traverse(self):
        utils = TraverserUtils()
        data = {"a": {"b": 1}, "c": 2}
        paths = [path for path, _ in utils.traverse(data)]
        assert "a" in paths
        assert "a.b" in paths
        assert "c" in paths

    def test_report(self):
        utils = TraverserUtils()
        report = utils.report([("a", 1), ("a.b", 2)])
        assert report.paths == ["a", "a.b"]
