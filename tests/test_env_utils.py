#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du env_utils.py
"""

from agents.env_utils import EnvUtils, EnvReport


class TestEnvUtils:
    def test_get_existing(self, monkeypatch):
        monkeypatch.setenv("MY_VAR", "123")
        assert EnvUtils.get("MY_VAR") == "123"

    def test_get_missing(self):
        assert EnvUtils.get("MISSING_VAR", "default") == "default"

    def test_require(self, monkeypatch):
        monkeypatch.setenv("MY_VAR", "123")
        assert EnvUtils.require("MY_VAR") == "123"

    def test_require_missing(self):
        try:
            EnvUtils.require("MISSING_VAR")
            assert False, "Should have raised EnvironmentError"
        except EnvironmentError:
            pass

    def test_has(self, monkeypatch):
        monkeypatch.setenv("MY_VAR", "1")
        assert EnvUtils.has("MY_VAR") is True
        assert EnvUtils.has("MISSING_VAR") is False

    def test_report(self, monkeypatch):
        monkeypatch.setenv("MY_VAR", "123")
        r = EnvUtils.report("MY_VAR")
        assert r.name == "MY_VAR"
        assert r.found is True
        assert r.value == "123"
        assert r.timestamp
