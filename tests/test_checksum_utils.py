#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests du checksum_utils.py
"""

from agents.checksum_utils import ChecksumUtils, ChecksumReport


class TestChecksumUtils:
    def test_md5(self):
        assert ChecksumUtils.md5(b"abc") == "900150983cd24fb0d6963f7d28e17f72"

    def test_sha1(self):
        assert ChecksumUtils.sha1(b"abc") == "a9993e364706816aba3e25717850c26c9cd0d89d"

    def test_sha256(self):
        assert ChecksumUtils.sha256(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

    def test_checksums(self):
        result = ChecksumUtils.checksums("abc")
        assert set(result.keys()) == {"md5", "sha1", "sha256"}

    def test_report(self):
        report = ChecksumUtils.report("abc")
        assert report.text == "abc"
        assert "md5" in report.checksums
        assert report.timestamp
