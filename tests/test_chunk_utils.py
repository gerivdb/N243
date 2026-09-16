import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.chunk_utils import ChunkUtils


def test_chunk_inspect():
    chunks = ["chunk-1", "chunk-2", "chunk-3"]
    report = ChunkUtils.inspect(chunks)
    assert report.chunks == ["chunk-1", "chunk-2", "chunk-3"]
    assert report.timestamp
