#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du backup_utils.py
"""

from agents.backup_utils import BackupUtils


class TestBackupUtils:
    def test_filter(self):
        utils = BackupUtils()
        report = utils.filter([{"value": 1, "backup": True}, {"value": 2, "backup": False}])
        assert report.backup == [1]
