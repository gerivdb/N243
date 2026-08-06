"""
Integration tests for N243 sovereign cross-repo graph.
Validates the graph builder and query engine together.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

N243_DATA = Path("D:/DO/WEB/TOOLS/L4-TOOLS/N243/data")
SKILLS_ROOT = Path("D:/DO/WEB/TOOLS/SKILLS")


def test_graph_builder_produces_outputs():
    from n243_graph_builder.core import run_pipeline
    result = run_pipeline(N243_DATA)
    assert result.valid is True
    assert len(result.nodes) > 0
    assert "graph" in result.outputs
    assert "embeddings" in result.outputs
    assert "metadata" in result.outputs


def test_query_engine_uses_graph():
    from n243_query_engine import QueryRequest, QueryResult, execute
    result = execute(QueryRequest(query_type="topology"))
    assert result.ok is True
    assert result.meta["total_nodes"] > 0


def test_citizens_yaml_valid():
    import yaml
    citizens_path = Path("D:/DO/WEB/TOOLS/L4-TOOLS/N243/citizens.yaml")
    data = yaml.safe_load(citizens_path.read_text(encoding="utf-8"))
    assert "citizens" in data
    roles = {c["role"] for c in data["citizens"]}
    assert "builder" in roles
    assert "query" in roles
    assert "validator" in roles
    assert "orchestrator" in roles


def test_skills_exist():
    assert (SKILLS_ROOT / "n243-graph-builder/SKILL.md").exists()
    assert (SKILLS_ROOT / "n243-query-engine/SKILL.md").exists()


def test_skill_impls_exist():
    assert (SKILLS_ROOT / "n243-graph-builder/n243_graph_builder/__init__.py").exists()
    assert (SKILLS_ROOT / "n243-query-engine/n243_query_engine/__init__.py").exists()


def test_search_filters_nodes():
    from n243_query_engine import QueryRequest, execute
    result = execute(QueryRequest(query_type="search", target="GOVERNANCE-HUB"))
    assert result.ok is True
    assert len(result.items) > 0
