#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du zip_utils.py
"""

from agents.zip_utils import ZipUtils


class TestZipUtils:
    def test_apply(self):
        utils = ZipUtils()
        report = utils.apply([1, 2], ["a", "b"])
        assert report.zipped == [(1, "a"), (2, "b")]
