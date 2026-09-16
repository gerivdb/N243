#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du date_utils.py
"""

from agents.date_utils import DateUtils, DateReport


class TestDateUtils:
    def test_now_utc(self):
        iso = DateUtils.now_utc()
        assert iso.endswith("+00:00") or iso.endswith("Z")

    def test_is_future(self):
        future = "2099-01-01T00:00:00+00:00"
        past = "2000-01-01T00:00:00+00:00"
        assert DateUtils.is_future(future) is True
        assert DateUtils.is_future(past) is False

    def test_age_seconds(self):
        iso = "2000-01-01T00:00:00+00:00"
        age = DateUtils.age_seconds(iso)
        assert age > 0

    def test_report(self):
        report = DateUtils.report("2000-01-01T00:00:00+00:00")
        assert report.iso == "2000-01-01T00:00:00+00:00"
        assert report.is_future is False
        assert report.timestamp
