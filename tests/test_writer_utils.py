#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du writer_utils.py
"""

from agents.writer_utils import WriterUtils


class TestWriterUtils:
    def test_inspect(self):
        utils = WriterUtils()
        report = utils.inspect(["a", "b"], {"a": True, "b": False})
        assert report.written == ["a"]
