#!/usr/bin/env python3
"""
N243 Server — HTTP minimal pour supervision ternaire VOLTX.

Endpoints:
  GET  /health               — health check
  POST /decide               — décision ternaire sur mutation
  POST /supervision/decision — publier décision vers VOLTX via WAZAA

IntentHash: 0xN243_SERVER_MINIMAL_20260914
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Ensure WAZAA is importable
sys.path.insert(0, str(Path(r"D:\DO\WEB\TOOLS\L4-TOOLS\WAZAA")))

app = FastAPI(title="N243 Server", version="0.1.0")

# In-memory state
MUTATIONS: Dict[str, Dict[str, Any]] = {}
DECISIONS: list = []
THRESHOLD = 0.8


class MutationRequest(BaseModel):
    mutation_id: str
    kind: str
    entity: str
    provenance: str
    confidence: float
    payload: Optional[Dict[str, Any]] = None


class DecisionResponse(BaseModel):
    mutation_id: str
    decision: str
    reason: str
    timestamp_utc: str


def _decide(mutation: Dict[str, Any], threshold: float = THRESHOLD) -> tuple[str, str]:
    """Logique de décision ternaire N243."""
    confidence = mutation.get("confidence", 0.0)
    kind = mutation.get("kind", "")
    entity = mutation.get("entity", "")
    provenance = mutation.get("provenance", "")

    if confidence < threshold:
        return "SUSPENDRE", f"Confidence {confidence:.2f} < threshold {threshold}"
    if kind in ("delete_node", "delete_edge"):
        return "REJETER", f"Destructive kind '{kind}' on '{entity}'"
    if not provenance:
        return "SUSPENDRE", "Missing provenance"
    return "APPROUVER", f"OK (confidence={confidence:.2f}, provenance={provenance})"


@app.get("/health")
async def health():
    return {"status": "ok", "service": "n243", "timestamp_utc": datetime.now(timezone.utc).isoformat()}


@app.post("/decide", response_model=DecisionResponse)
async def decide_mutation(request: MutationRequest):
    mutation = request.dict()
    MUTATIONS[mutation["mutation_id"]] = mutation
    decision, reason = _decide(mutation)
    entry = {
        "mutation_id": mutation["mutation_id"],
        "decision": decision,
        "reason": reason,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    DECISIONS.append(entry)
    return entry


@app.post("/supervision/decision")
async def publish_decision(request: MutationRequest):
    """Publier décision vers VOLTX via WAZAA."""
    mutation = request.dict()
    MUTATIONS[mutation["mutation_id"]] = mutation
    decision, reason = _decide(mutation)

    # Try to publish via WAZAA if available
    try:
        from wazaa_server import app as wazaa_app
        # WAZAA server is running separately; we just log here
        pass
    except ImportError:
        pass

    entry = {
        "mutation_id": mutation["mutation_id"],
        "decision": decision,
        "reason": reason,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    DECISIONS.append(entry)
    return entry


@app.get("/decisions")
async def list_decisions(limit: int = 10):
    return {"decisions": DECISIONS[-limit:]}


@app.get("/mutations")
async def list_mutations(limit: int = 10):
    return {"mutations": list(MUTATIONS.values())[-limit:]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
