#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du prd_moc_supervisor.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

N243_ROOT = Path(r"D:\DO\WEB\TOOLS\L4-TOOLS\N243")
sys.path.insert(0, str(N243_ROOT / "agents"))

from agents.prd_moc_supervisor import N243Supervisor, TernaryWAL


class TestTernaryWAL:
    def test_append_and_read(self, tmp_path):
        wal = TernaryWAL(tmp_path / "wal.jsonl")
        wal.append("APPROUVER", "VOLTX", {"score": 0.97})
        wal.append("SUSPENDRE", "VOLTX", {"score": 0.85})
        entries = wal.read_last(2)
        assert len(entries) == 2
        assert entries[0]["verdict"] == "APPROUVER"
        assert entries[1]["verdict"] == "SUSPENDRE"

    def test_read_last_empty(self, tmp_path):
        wal = TernaryWAL(tmp_path / "empty.jsonl")
        entries = wal.read_last(5)
        assert entries == []

    def test_timestamp_present(self, tmp_path):
        wal = TernaryWAL(tmp_path / "wal.jsonl")
        wal.append("APPROUVER", "REPO", {})
        entries = wal.read_last(1)
        assert "timestamp" in entries[0]


class TestN243Supervisor:
    def test_supervise_approve(self, tmp_path):
        wal_path = tmp_path / "test-approve.jsonl"
        supervisor = N243Supervisor(wal_path=wal_path)
        decision = supervisor.supervise("VOLTX", "APPROUVER", {"score": 0.97})
        assert decision["verdict"] == "APPROUVER"
        assert decision["action"] == "execute"
        assert "timestamp" in decision

    def test_supervise_suspend(self, tmp_path):
        wal_path = tmp_path / "test-suspend.jsonl"
        supervisor = N243Supervisor(wal_path=wal_path)
        decision = supervisor.supervise("VOLTX", "SUSPENDRE", {"score": 0.85})
        assert decision["verdict"] == "SUSPENDRE"
        assert decision["action"] == "pending"

    def test_supervise_reject(self, tmp_path):
        wal_path = tmp_path / "test-reject.jsonl"
        supervisor = N243Supervisor(wal_path=wal_path)
        decision = supervisor.supervise("VOLTX", "REJETER", {"score": 0.4})
        assert decision["verdict"] == "REJETER"
        assert decision["action"] == "archive"

    def test_supervise_unknown_verdict(self, tmp_path):
        wal_path = tmp_path / "test-unknown.jsonl"
        supervisor = N243Supervisor(wal_path=wal_path)
        decision = supervisor.supervise("VOLTX", "INCONNU", {})
        assert decision["action"] == "unknown"

    def test_narrative(self, tmp_path):
        wal_path = tmp_path / "test-narrative.jsonl"
        supervisor = N243Supervisor(wal_path=wal_path)
        supervisor.supervise("VOLTX", "APPROUVER", {"score": 0.97})
        narrative = supervisor.narrative()
        assert "N243 Supervision Narrative" in narrative
        assert "APPROUVER" in narrative

    def test_last_decisions(self, tmp_path):
        wal_path = tmp_path / "test-last.jsonl"
        supervisor = N243Supervisor(wal_path=wal_path)
        supervisor.supervise("VOLTX", "APPROUVER", {})
        supervisor.supervise("VOLTX", "SUSPENDRE", {})
        decisions = supervisor.last_decisions(1)
        assert len(decisions) == 1
        assert decisions[0]["verdict"] == "SUSPENDRE"

    def test_validate_frontmatter_valid(self, tmp_path):
        supervisor = N243Supervisor()
        content = '---\ntype: PRD-MOC\nversion: "1.0.0"\ndate: "2026-09-16"\nstatus: proposed\nintent_hash: 0xTEST_20260916\n---\n# Title\n'
        path = tmp_path / "valid.md"
        path.write_text(content, encoding="utf-8")
        result = supervisor.validate_frontmatter(path)
        assert result["valid"] is True
        assert result["verdict"] == "APPROUVER"

    def test_validate_frontmatter_missing_fields(self, tmp_path):
        supervisor = N243Supervisor()
        content = "---\ntype: PRD\n---\n# Title\n"
        path = tmp_path / "invalid.md"
        path.write_text(content, encoding="utf-8")
        result = supervisor.validate_frontmatter(path)
        assert result["valid"] is False
        assert result["verdict"] == "REJETER"
        assert any("Missing required fields" in e for e in result["errors"])

    def test_validate_frontmatter_invalid_type(self, tmp_path):
        supervisor = N243Supervisor()
        content = "---\ntype: INVALID\nversion: '1.0.0'\ndate: '2026-09-16'\nstatus: proposed\nintent_hash: 0xTEST\n---\n# Title\n"
        path = tmp_path / "invalid.md"
        path.write_text(content, encoding="utf-8")
        result = supervisor.validate_frontmatter(path)
        assert result["valid"] is False
        assert any("Invalid type" in e for e in result["errors"])

    def test_validate_frontmatter_missing_block(self, tmp_path):
        supervisor = N243Supervisor()
        content = "# No frontmatter\n"
        path = tmp_path / "nofm.md"
        path.write_text(content, encoding="utf-8")
        result = supervisor.validate_frontmatter(path)
        assert result["valid"] is False
        assert any("Missing YAML frontmatter block" in e for e in result["errors"])
