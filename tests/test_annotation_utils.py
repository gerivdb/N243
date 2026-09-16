import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.annotation_utils import AnnotationUtils


def test_annotation_inspect():
    annotations = ["anno-1", "anno-2", "anno-3"]
    report = AnnotationUtils.inspect(annotations)
    assert report.annotations == ["anno-1", "anno-2", "anno-3"]
    assert report.timestamp
