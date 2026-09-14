#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_n243_supervisor.py — Tests N243 supervisor avec TALEX governance.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

N243_ROOT = Path(r"D:\DO\WEB\TOOLS\L4-TOOLS\N243")
sys.path.insert(0, str(N243_ROOT / "agents"))

from prd_moc_supervisor import N243Supervisor, TernaryWAL


def test_ternary_wal(tmp_path: Path) -> None:
    wal = TernaryWAL(tmp_path / "wal.jsonl")
    wal.append("APPROUVER", "VOLTX", {"score": 0.97})
    wal.append("SUSPENDRE", "VOLTX", {"score": 0.85})
    entries = wal.read_last(2)
    assert len(entries) == 2
    assert entries[0]["verdict"] == "APPROUVER"
    assert entries[1]["verdict"] == "SUSPENDRE"
    print("[TEST] test_ternary_wal OK")


def test_n243_supervisor_approve() -> None:
    wal_path = N243_ROOT / "WAL" / "test-n243-approve.jsonl"
    supervisor = N243Supervisor(wal_path=wal_path)
    decision = supervisor.supervise("VOLTX", "APPROUVER", {"score": 0.97})
    assert decision["verdict"] == "APPROUVER"
    assert decision["action"] == "execute"
    assert "talex_context" in decision
    print("[TEST] test_n243_supervisor_approve OK")


def test_n243_supervisor_suspend() -> None:
    wal_path = N243_ROOT / "WAL" / "test-n243-suspend.jsonl"
    supervisor = N243Supervisor(wal_path=wal_path)
    decision = supervisor.supervise("VOLTX", "SUSPENDRE", {"score": 0.85})
    assert decision["verdict"] == "SUSPENDRE"
    assert decision["action"] == "pending"
    print("[TEST] test_n243_supervisor_suspend OK")


def test_n243_supervisor_reject() -> None:
    wal_path = N243_ROOT / "WAL" / "test-n243-reject.jsonl"
    supervisor = N243Supervisor(wal_path=wal_path)
    decision = supervisor.supervise("VOLTX", "REJETER", {"score": 0.4})
    assert decision["verdict"] == "REJETER"
    assert decision["action"] == "archive"
    print("[TEST] test_n243_supervisor_reject OK")


def test_n243_narrative() -> None:
    wal_path = N243_ROOT / "WAL" / "test-n243-narrative.jsonl"
    supervisor = N243Supervisor(wal_path=wal_path)
    supervisor.supervise("VOLTX", "APPROUVER", {"score": 0.97})
    supervisor.supervise("VOLTX", "SUSPENDRE", {"score": 0.85})
    narrative = supervisor.narrative()
    assert "N243 Supervision Narrative" in narrative
    assert "APPROUVER" in narrative
    assert "SUSPENDRE" in narrative
    print("[TEST] test_n243_narrative OK")


def main() -> int:
    test_ternary_wal(N243_ROOT / "WAL" / "test")
    test_n243_supervisor_approve()
    test_n243_supervisor_suspend()
    test_n243_supervisor_reject()
    test_n243_narrative()
    print("[TEST] ALL TESTS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
