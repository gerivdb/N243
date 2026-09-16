#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
path_utils.py — N243 Path Utils

Rôle :
- Fournir des manipulations simples de chemins
- Basename, dirname, extension, join, exists
- Publier un rapport de chemin
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class PathReport:
    path: str
    basename: str
    dirname: str
    extension: str
    timestamp: str


class PathUtils:
    @staticmethod
    def basename(path: str) -> str:
        return os.path.basename(path)

    @staticmethod
    def dirname(path: str) -> str:
        return os.path.dirname(path)

    @staticmethod
    def ext(path: str) -> str:
        _, ext = os.path.splitext(path)
        return ext

    @staticmethod
    def join(*parts: str) -> str:
        return os.path.join(*parts)

    @staticmethod
    def exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def report(path: str) -> PathReport:
        return PathReport(
            path=path,
            basename=PathUtils.basename(path),
            dirname=PathUtils.dirname(path),
            extension=PathUtils.ext(path),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
