"""Main Crew"""

from dotenv import load_dotenv
from crewai import Crew, Process
from tasks import QueryTasks
from agents import QueryAgents

agents = QueryAgents()
tasks = QueryTasks()

crew = Crew(
    tasks=[tasks.query_extraction_task(), tasks.query_construction_task()],
    agents=[agents.extractor_agent(), agents.query_constructor()],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)

if __name__ == "__main__":
    load_dotenv()

    crew.kickoff()


#TODO: okay the crew works with the search tool as well (tavily).
# But the task is randomly generating a user query -> how do i pass the human in the loop for input? 

# NOTE: what's the difference between passing the tool to the task vs the agent?
