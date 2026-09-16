import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.import_utils import ImportUtils


def test_import_inspect():
    imports = ["import-1", "import-2", "import-3"]
    report = ImportUtils.inspect(imports)
    assert report.imports == ["import-1", "import-2", "import-3"]
    assert report.timestamp
