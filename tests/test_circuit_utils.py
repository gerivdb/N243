import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.circuit_utils import CircuitUtils


def test_circuit_inspect():
    circuits = ["circuit-1", "circuit-2", "circuit-3"]
    report = CircuitUtils.inspect(circuits)
    assert report.circuits == ["circuit-1", "circuit-2", "circuit-3"]
    assert report.timestamp
