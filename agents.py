"""Agents module."""

import os
from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class QueryAgents:
    """Agents for the Query Constructions."""

    turbo = ChatOpenAI(model="gpt-3.5-turbo")

    tavily_search_tool = TavilySearchResults()

    def extractor_agent(self) -> Agent:
        return Agent(
            role="Extractor Agent",
            goal="Extract what is the statistic to search for from the user's query",
            backstory="""You are a great extractor.
            You will extrct the statistic to search for from the user query.
            """,
            llm=self.turbo,
            allow_delegation=True,
            verbose=True,
        )

    def query_constructor(self) -> Agent:
        return Agent(
            role="Query Constructor",
            goal="Construct a query to search for the statistic online",
            backstory="""You are an expert online searcher. Given the statistics,
            you will construct a perfect query to search for the statistic online. 
            You will then use the search tool to search for the statistic.
            """,
            llm=self.turbo,
            tools=[self.tavily_search_tool],
            allow_delegation=True,
            verbose=True,
        )
