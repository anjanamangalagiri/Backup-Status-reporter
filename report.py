import csv
from collections import Counter

def read_jobs(path):
    """Read the CSV and return a list of job dictionaries."""
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def summarize(jobs):
    """Return total jobs, success count and success rate (percent)."""
    total = len(jobs)
    # TODO: count the jobs whose status is "Success"
    # TODO: success rate = success / total * 100
    # return total, success, rate

def failures_by_workload(jobs):
    """Return a Counter of failed jobs per workload."""
    # TODO: look at jobs whose status is "Failed"
    # and count them by their "workload" value

if __name__ == "__main__":
    jobs = read_jobs("sample_jobs.csv")
    total, success, rate = summarize(jobs)
    print("Total jobs:", total)
    print("Successful:", success)
    print(f"Success rate: {rate:.1f}%")
    print("Failures by workload:", failures_by_workload(jobs))