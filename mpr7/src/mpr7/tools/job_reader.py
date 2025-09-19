# src/mpr7/tools/job_reader.py
import csv
from pathlib import Path
from crewai.tools import BaseTool

class JobReaderTool(BaseTool):
    name: str = "job_reader"
    description: str = "Reads jobs from jobs/jobs.csv and returns them as a markdown table."

    def _run(self, file_path: str = "jobs/jobs.csv") -> str:
        jobs_file = Path(file_path)
        if not jobs_file.exists():
            return "No jobs file found."

        with open(jobs_file, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            jobs = [row for row in reader]

        output = "| Job ID | Duration | Type |\n|--------|----------|------|\n"
        for job in jobs:
            output += f"| {job['job_id']} | {job['duration']} | {job['type']} |\n"
        return output
