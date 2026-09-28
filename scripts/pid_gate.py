#!/usr/bin/env python3
"""N243 PID Gate — Validate PIDs before acceptance into the ecosystem."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from n243.validators.pid_gate import validate_pid


def main() -> int:
    parser = argparse.ArgumentParser(description="N243 PID Gate")
    parser.add_argument("--pid", type=int, required=True)
    parser.add_argument("--citizen", type=str, required=True)
    parser.add_argument("--daemon", type=str, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result = validate_pid(args.pid, args.citizen, args.daemon)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        verdict = result.get("verdict", "unknown")
        print(f"[N243] PID {args.pid} {args.citizen}/{args.daemon}: {verdict}")
        if result.get("errors"):
            for err in result["errors"]:
                print(f"  ERROR: {err}")
        if result.get("warnings"):
            for warn in result["warnings"]:
                print(f"  WARN: {warn}")
        return 0 if verdict == "accept" else 2


if __name__ == "__main__":
    sys.exit(main())
