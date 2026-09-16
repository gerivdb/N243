import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.classifier_utils import ClassifierUtils


def test_classifier_inspect():
    classes = ["class-1", "class-2", "class-3"]
    report = ClassifierUtils.inspect(classes)
    assert report.classes == ["class-1", "class-2", "class-3"]
    assert report.timestamp
