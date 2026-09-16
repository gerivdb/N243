import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.audit_utils import AuditUtils


def test_audit_inspect():
    audits = ["audit-1", "audit-2", "audit-3"]
    report = AuditUtils.inspect(audits)
    assert report.audits == ["audit-1", "audit-2", "audit-3"]
    assert report.timestamp
