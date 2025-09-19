from crewai import Task
from mpr7.config.agents import manager, worker1, worker2, worker3

scheduling_task = Task(
    description=(
        "Read jobs from the CSV using job_reader. "
        "Assign jobs to the correct machine and build a schedule table."
    ),
    expected_output="A schedule table with job, type, machine, start and end times",
    agent=manager
)

execution_task_worker1 = Task(
    description="Execute jobs of type handled by Worker 1. Confirm with job_id, machine, start, and finish status.",
    expected_output="Execution log for Worker 1 with job_id, machine, start time, and completion status.",
    agent=worker1
)

execution_task_worker2 = Task(
    description="Execute jobs of type handled by Worker 2. Confirm with job_id, machine, start, and finish status.",
    expected_output="Execution log for Worker 2 with job_id, machine, start time, and completion status.",
    agent=worker2
)

execution_task_worker3 = Task(
    description="Execute jobs of type handled by Worker 3. Confirm with job_id, machine, start, and finish status.",
    expected_output="Execution log for Worker 3 with job_id, machine, start time, and completion status.",
    agent=worker3
)