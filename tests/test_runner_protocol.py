"""
Runner protocol integration tests for N243.

Validates:
- Supervisor can process runner protocol decisions
- WAL records runner decisions correctly
- Frontmatter validation integrates with runner workflow
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path("D:/DO/WEB/TOOLS/L4-TOOLS/N243/agents")))

import json

import pytest

from prd_moc_supervisor import N243Supervisor, TernaryWAL

N243_ROOT = Path("D:/DO/WEB/TOOLS/L4-TOOLS/N243")


def test_wal_records_runner_decision(tmp_path):
    wal = TernaryWAL(tmp_path / "runner-wal.jsonl")
    supervisor = N243Supervisor(wal_path=tmp_path / "runner-wal.jsonl")
    decision = supervisor.supervise(
        repo="N243",
        verdict="APPROUVER",
        payload={
            "runner": "LLUX",
            "protocol": "runner_protocol",
            "l5_verdict": "Approved",
            "l6_proof": "valid",
        },
    )
    assert decision["action"] == "execute"
    entries = wal.read_last(1)
    assert len(entries) == 1
    assert entries[0]["verdict"] == "APPROUVER"
    assert entries[0]["repo"] == "N243"


def test_supervisor_validates_prd_frontmatter_before_runner_gate():
    supervisor = N243Supervisor()
    prd_path = N243_ROOT / "PRD" / "PRD-N243-001-gate-orchestration-runner-protocol.md"
    result = supervisor.validate_frontmatter(prd_path)
    assert result["valid"] is True
    assert result["verdict"] == "APPROUVER"
    assert result["frontmatter"]["type"] == "PRD-MOC"
    assert result["frontmatter"]["status"] == "proposed"


def test_runner_decision_suspend_creates_pending_action():
    supervisor = N243Supervisor()
    decision = supervisor.supervise(
        repo="N243",
        verdict="SUSPENDRE",
        payload={"runner": "RLM-243", "reason": "awaiting L6 proof"},
    )
    assert decision["action"] == "pending"
    assert "suspendue" in decision["message"]


def test_runner_decision_reject_creates_archive_action():
    supervisor = N243Supervisor()
    decision = supervisor.supervise(
        repo="N243",
        verdict="REJETER",
        payload={"runner": "TIMX", "reason": "invalid functor"},
    )
    assert decision["action"] == "archive"
    assert "rejetée" in decision["message"]


def test_supervisor_wazaa_topic_is_prd_moc_gate(monkeypatch, tmp_path):
    """S3.2 — Le supervisor publie sur le topic WAZAA prd_moc.gate"""
    calls: list = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        class FakeResult:
            returncode = 0
            stdout = b""
            stderr = b""
        return FakeResult()

    monkeypatch.setattr("subprocess.run", fake_run)
    fake_wazaa = tmp_path / "wazaa_bus.py"
    fake_wazaa.write_text("", encoding="utf-8")
    monkeypatch.setattr("prd_moc_supervisor.WAZAA_BUS", fake_wazaa)

    supervisor = N243Supervisor()
    decision = supervisor.supervise(
        repo="N243",
        verdict="APPROUVER",
        payload={"runner": "LLUX"},
    )

    wazaa_calls = [cmd for cmd in calls if "prd_moc.gate" in cmd]
    assert len(wazaa_calls) >= 1, f"Expected WAZAA publish call, got: {calls}"
    payload = json.loads(wazaa_calls[0][4])
    assert payload["verdict"] == "APPROUVER"
    assert payload["repo"] == "N243"
