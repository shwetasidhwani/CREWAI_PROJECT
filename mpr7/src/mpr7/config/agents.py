from crewai import Agent, Task, Crew, Process
from mpr7.tools.job_reader import JobReaderTool

manager = Agent(
    role="Production Coordinator",
    goal="Assign jobs to machines based on specialization and availability",
    backstory="You are the coordinator of the factory",
    tools=[JobReaderTool()],  # <-- instantiate your tool here
)

worker1 = Agent(
    role="Cutting Machine",
    goal="Execute cutting jobs efficiently.",
    backstory="Handles only 'cutting' tasks.",
    verbose=True,
)

worker2 = Agent(
    role="Welding Machine",
    goal="Execute welding jobs reliably.",
    backstory="Handles only 'welding' tasks.",
    verbose=True,
)

worker3 = Agent(
    role="Assembly Machine",
    goal="Assemble components into finished products.",
    backstory="Handles only 'assembly' tasks.",
    verbose=True,
)

