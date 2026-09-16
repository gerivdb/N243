import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.cipher_utils import CipherUtils


def test_cipher_inspect():
    encrypts = ["enc-1", "enc-2", "enc-3"]
    report = CipherUtils.inspect(encrypts)
    assert report.encrypts == ["enc-1", "enc-2", "enc-3"]
    assert report.timestamp
