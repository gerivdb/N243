import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from agents.job_utils import JobUtils


def test_job_inspect():
    jobs = ["job-1", "job-2", "job-3"]
    report = JobUtils.inspect(jobs)
    assert report.jobs == ["job-1", "job-2", "job-3"]
    assert report.timestamp
