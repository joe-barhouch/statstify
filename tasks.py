"""Tasks module."""

from crewai import Task
from agents import QueryAgents

agents = QueryAgents()


class QueryTasks:
    def query_extraction_task(self) -> Task:
        return Task(
            description="Extract the statistic to search for from the user query",
            expected_output="The statistic to search for",
            agent=agents.extractor_agent(),
            human_input=True,
            output_file="stasts.txt",
        )

    def query_construction_task(self) -> Task:
        return Task(
            description="Construct a query to search for the statistic online",
            expected_output="The search results",
            agent=agents.query_constructor(),
            output_file="search_queries.txt",
        )
