"""Tests for N243 PID gate validator."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# Ensure src is importable when running tests from repo root
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from n243.validators.pid_gate import validate_pid


def test_validate_pid_accepts_valid_pid(tmp_path: Path):
    result = validate_pid(12345, "LOOPX", "loopx-daemon")
    assert result["verdict"] == "accept"
    assert result["errors"] == []
    assert result["warnings"] == []


def test_validate_pid_rejects_zero_pid():
    result = validate_pid(0, "LOOPX", "loopx-daemon")
    assert result["verdict"] == "reject"
    assert "PID must be a positive integer" in result["errors"]


def test_validate_pid_rejects_negative_pid():
    result = validate_pid(-1, "LOOPX", "loopx-daemon")
    assert result["verdict"] == "reject"
    assert "PID must be a positive integer" in result["errors"]


def test_validate_pid_rejects_missing_citizen():
    result = validate_pid(12345, "", "loopx-daemon")
    assert result["verdict"] == "reject"
    assert "citizen is required" in result["errors"]


def test_validate_pid_rejects_missing_daemon_id():
    result = validate_pid(12345, "LOOPX", "")
    assert result["verdict"] == "reject"
    assert "daemon_id is required" in result["errors"]


def test_validate_pid_rejects_non_integer_pid():
    result = validate_pid("abc", "LOOPX", "loopx-daemon")
    assert result["verdict"] == "reject"
    assert "PID must be a positive integer" in result["errors"]
