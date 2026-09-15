#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du assembler_utils.py
"""

from agents.assembler_utils import AssemblerUtils


class TestAssemblerUtils:
    def test_assemble(self):
        utils = AssemblerUtils()
        assert utils.assemble(["a", "b", "c"]) == "abc"
        assert utils.assemble(["a", "b", "c"], "-") == "a-b-c"

    def test_report(self):
        utils = AssemblerUtils()
        result = utils.report(["a", "b"], "ab")
        assert result.parts == 2
        assert result.result == "ab"
