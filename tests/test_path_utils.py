#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du path_utils.py
"""

from agents.path_utils import PathUtils, PathReport
import os


class TestPathUtils:
    def test_basename(self):
        assert PathUtils.basename("/path/to/file.txt") == "file.txt"

    def test_dirname(self):
        assert PathUtils.dirname("/path/to/file.txt") == "/path/to"

    def test_ext(self):
        assert PathUtils.ext("/path/to/file.txt") == ".txt"

    def test_join(self):
        assert PathUtils.join("a", "b", "c") == os.path.join("a", "b", "c")

    def test_report(self):
        r = PathUtils.report("/path/to/file.txt")
        assert r.path == "/path/to/file.txt"
        assert r.basename == "file.txt"
        assert r.extension == ".txt"
        assert r.timestamp
