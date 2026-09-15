#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du validator_utils.py
"""

from agents.validator_utils import ValidatorUtils


class TestValidatorUtils:
    def test_validate_valid(self):
        utils = ValidatorUtils()
        report = utils.validate({"a": 1}, ["a"])
        assert report.valid is True
        assert report.missing == []

    def test_validate_invalid(self):
        utils = ValidatorUtils()
        report = utils.validate({"a": 1}, ["a", "b"])
        assert report.valid is False
        assert report.missing == ["b"]
