#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decorator_utils.py — N243 Decorator Utils

Rôle :
- Fournir des décorateurs simples (retry, log_call)
- Publier un rapport de décoration
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


@dataclass
class DecoratorReport:
    function_name: str
    attempts: int
    success: bool
    timestamp: str


def retry(attempts: int = 3, delay: float = 0.0):
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:  # noqa: BLE001
                    last_error = exc
                    if delay > 0:
                        time.sleep(delay)
            raise last_error

        return wrapper  # type: ignore[return-value]

    return decorator


def log_call(func: F) -> F:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"CALL {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]


def report(function_name: str, attempts: int, success: bool) -> DecoratorReport:
    return DecoratorReport(
        function_name=function_name,
        attempts=attempts,
        success=success,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
