#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du migration_utils.py
"""

from agents.migration_utils import MigrationUtils


class TestMigrationUtils:
    def test_filter(self):
        utils = MigrationUtils()
        report = utils.filter([{"value": 1, "migration": True}, {"value": 2, "migration": False}])
        assert report.migrated == [1]
