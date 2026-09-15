#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du validator_schema_utils.py
"""

from agents.validator_schema_utils import ValidatorSchemaUtils


class TestValidatorSchemaUtils:
    def test_validate_fields_missing(self):
        utils = ValidatorSchemaUtils()
        assert utils.validate_fields({"a": 1}, ["a", "b"]) == ["b"]

    def test_report_valid(self):
        utils = ValidatorSchemaUtils()
        report = utils.report({"a": 1}, ["a"])
        assert report.valid is True
        assert report.missing_fields == []

    def test_report_invalid(self):
        utils = ValidatorSchemaUtils()
        report = utils.report({"a": 1}, ["a", "b"])
        assert report.valid is False
        assert report.missing_fields == ["b"]
