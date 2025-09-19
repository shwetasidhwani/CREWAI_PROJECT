from crewai import Agent, Task, Crew, Process
from mpr7.config.agents import manager, worker1, worker2, worker3
from mpr7.config.tasks import scheduling_task, execution_task_worker1, execution_task_worker2, execution_task_worker3


def create_crew():
    return Crew(
        agents=[manager, worker1, worker2, worker3],
        tasks=[scheduling_task, execution_task_worker1, execution_task_worker2, execution_task_worker3],
        process=Process.sequential
    )
