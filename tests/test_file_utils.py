import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.file_utils import FileUtils


def test_file_inspect():
    files = ["file-1.txt", "file-2.txt", "file-3.txt"]
    report = FileUtils.inspect(files)
    assert report.files == ["file-1.txt", "file-2.txt", "file-3.txt"]
    assert report.timestamp
