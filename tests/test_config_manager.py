#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du config_manager.py
"""

from agents.config_manager import ConfigManager


class TestConfigManager:
    def test_get_with_env(self):
        manager = ConfigManager({"timeout": 10})
        manager.add_environment("prod", {"timeout": 30, "retries": 3})
        assert manager.get("prod", "timeout") == 30
        assert manager.get("prod", "retries") == 3

    def test_get_fallback_to_defaults(self):
        manager = ConfigManager({"timeout": 10})
        manager.add_environment("prod", {"retries": 3})
        assert manager.get("prod", "timeout") == 10
        assert manager.get("unknown", "timeout") == 10
        assert manager.get("unknown", "missing", "fallback") == "fallback"
