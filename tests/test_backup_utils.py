import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.backup_utils import BackupUtils


def test_backup_inspect():
    backups = ["backup-1", "backup-2", "backup-3"]
    report = BackupUtils.inspect(backups)
    assert report.backups == ["backup-1", "backup-2", "backup-3"]
    assert report.timestamp
