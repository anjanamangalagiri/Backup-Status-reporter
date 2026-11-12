import csv

def read_jobs(path):
    """Read the CSV and return a list of job dictionaries."""
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

if __name__ == "__main__":
    jobs = read_jobs("sample_jobs.csv")
    print("Total jobs:", len(jobs))
    print("First job:", jobs[0])