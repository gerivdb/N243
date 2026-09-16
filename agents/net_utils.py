#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
net_utils.py — N243 Net Utils

Rôle :
- Fournir des utilitaires simples de manipulation d'URLs
- Parser, ajouter des paramètres de requête, extraire la base
- Publier un rapport de manipulation URL
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import urlencode, urlparse, urlunparse, parse_qs
from typing import Optional


@dataclass
class NetReport:
    url: str
    result: str
    timestamp: str


class NetUtils:
    @staticmethod
    def parse(url: str) -> dict:
        parsed = urlparse(url)
        return {
            "scheme": parsed.scheme,
            "netloc": parsed.netloc,
            "path": parsed.path,
            "query": parsed.query,
        }

    @staticmethod
    def add_query(url: str, params: dict) -> str:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        query.update({key: [str(value)] for key, value in params.items()})
        new_query = urlencode({key: values[0] for key, values in query.items()})
        return urlunparse(parsed._replace(query=new_query))

    @staticmethod
    def base(url: str) -> str:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"

    @staticmethod
    def report(url: str, operation: str) -> NetReport:
        return NetReport(
            url=url,
            result=NetUtils.base(url) if operation == "base" else url,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
